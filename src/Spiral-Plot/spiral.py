import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv("melbourne2008-2010.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)

df["Year"]     = df["Date"].dt.year
df["TempMin"]  = df["temperature_2m_min"]
df["TempMax"]  = df["temperature_2m_max"]
df["YearMean"] = df.groupby("Year")["TempMin"].transform("mean")
df["Diff"]     = df["TempMin"] - df["YearMean"]

n     = len(df)
years = sorted(df["Year"].unique())
turns = len(years)

df["theta"]  = 360 * (df.index / n * turns)
df["radius"] = 1 + df.index / n * 5

# Escala de temperatura 
T_min_g  = df["TempMin"].min()
T_max_g  = df["TempMax"].max()
T_range  = T_max_g - T_min_g
bar_scale = 1.5 

colors      = ["#4e9af1", "#f4a742", "#5ecf7a"]
colors_fill = ["rgba(78,154,241,0.18)", "rgba(244,167,66,0.18)", "rgba(94,207,122,0.18)"]

fig = go.Figure()

# rango TempMin-TempMax
for i, y in enumerate(years):
    d    = df[df["Year"] == y]
    r_hi = d["radius"] + (d["TempMax"] - T_min_g) / T_range * bar_scale
    r_lo = d["radius"] + (d["TempMin"] - T_min_g) / T_range * bar_scale

    r_fill = list(r_hi) + list(r_lo.iloc[::-1])
    t_fill = list(d["theta"]) + list(d["theta"].iloc[::-1])

    fig.add_trace(go.Scatterpolar(
        r=r_fill, theta=t_fill,
        fill="toself", fillcolor=colors_fill[i],
        line=dict(width=0),
        showlegend=False, hoverinfo="skip"
    ))

# Barras
bar_width = 360 / n * turns * 0.4  
offset    = bar_width * 0.5          

for i, y in enumerate(years):
    d      = df[df["Year"] == y]
    r_min  = (d["TempMin"] - T_min_g) / T_range * bar_scale
    r_max  = (d["TempMax"] - T_min_g) / T_range * bar_scale

    # Barra TempMin
    fig.add_trace(go.Barpolar(
        r=r_min.values,
        base=d["radius"].values,
        theta=(d["theta"] - offset).values,
        width=bar_width,
        marker=dict(color="#4e9af1", opacity=0.6, line=dict(width=0)),
        showlegend=False,
        hoverinfo="skip"
    ))

    # Barra TempMax
    fig.add_trace(go.Barpolar(
        r=r_max.values,
        base=d["radius"].values,
        theta=(d["theta"] + offset).values,
        width=bar_width,
        marker=dict(color="#f45c4e", opacity=0.6, line=dict(width=0)),
        showlegend=False,
        hoverinfo="skip"
    ))

# Lineas de la espiral 
for i, y in enumerate(years):
    d = df[df["Year"] == y]
    fig.add_trace(go.Scatterpolar(
        r=d["radius"], theta=d["theta"],
        mode="lines",
        line=dict(color=colors[i], width=2.5),
        name=str(y),
        hovertemplate=(
            "<b>%{text}</b><br>"
            "Fecha: %{customdata[0]}<br>"
            "Temp mín: %{customdata[1]:.1f}°C<br>"
            "Temp máx: %{customdata[2]:.1f}°C<br>"
            "Diferencia anual: %{customdata[3]:.2f}°C<br>"
            "<extra></extra>"
        ),
        text=[f"Año {y}"] * len(d),
        customdata=np.stack([
            d["Date"].dt.strftime("%Y-%m-%d"),
            d["TempMin"], d["TempMax"], d["Diff"]
        ], axis=-1)
    ))

# etiquetas de mes y año 
month_es = ["ENE","FEB","MAR","ABR","MAY","JUN",
            "JUL","AGO","SEP","OCT","NOV","DIC"]

lbl_r, lbl_t, lbl_txt = [], [], []
yr_r,  yr_t,  yr_txt  = [], [], []

for _, row in df.iterrows():
    if row["Date"].day == 1:
        lbl_r.append(row["radius"] + 0.22)
        lbl_t.append(row["theta"])
        lbl_txt.append(month_es[row["Date"].month - 1])
        if row["Date"].month == 1:
            yr_r.append(row["radius"] + 0.55)
            yr_t.append(row["theta"])
            yr_txt.append(f"<b>{int(row['Year'])}</b>")

fig.add_trace(go.Scatterpolar(
    r=lbl_r, theta=lbl_t,
    mode="text", text=lbl_txt,
    textfont=dict(size=7, color="rgba(200,200,200,0.65)"),
    showlegend=False, hoverinfo="skip"
))
fig.add_trace(go.Scatterpolar(
    r=yr_r, theta=yr_t,
    mode="text", text=yr_txt,
    textfont=dict(size=12, color="white"),
    showlegend=False, hoverinfo="skip"
))

# Layout modo noche
fig.update_layout(
    title=dict(
        text="<b>Espiral de Temperatura - Melbourne (2008–2010)</b>",
        font=dict(color="white", size=16), x=0.5
    ),
    hoverlabel=dict(
        font_size=13,
        namelength=-1  
    ),
    showlegend=True,
    legend=dict(font=dict(color="white"), bgcolor="rgba(0,0,0,0)"),
    polar=dict(
        bgcolor="#111",
        radialaxis=dict(visible=False),
        angularaxis=dict(visible=False)
    ),
    width=900, height=900,
    margin=dict(l=50, r=50, t=80, b=50),
    paper_bgcolor="#111",
    font=dict(color="white")
)

fig.add_annotation(
    text='Fuente: <a href="https://github.com/acakin/weatherAUS/blob/master/meteo_api.csv" '
         'style="color:#aaaaaa;">acakin/weatherAUS – meteo_api.csv</a>',
    xref="paper", yref="paper",
    x=0.5, y=1.04,        
    showarrow=False,
    font=dict(size=11, color="#888888"),
    align="center"
)

html = fig.to_html(full_html=False, include_plotlyjs="cdn")
html_page = f"""<html>
<head><style>
body {{ display:flex; justify-content:center; align-items:center;
       height:100vh; margin:0; background:#111; }}
</style></head>
<body>{html}</body>
</html>"""

with open("spiral.html", "w", encoding="utf-8") as f:
    f.write(html_page)
print("Archivo generado: spiral.html")