import plotly.express as px
import pandas as pd
# Datos reales de 2016 (resumen)
# Fuentes:
# https://upload.wikimedia.org/wikipedia/commons/0/09/2016_US_Presidential_Election_Pie_Charts.png
# https://en.wikipedia.org/wiki/2016_United_States_presidential_election

data = {
    # Estados
    "state": [
        "Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida",
        "Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine",
        "Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska",
        "Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota",
        "Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
        "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"
    ],
    
    # Latitud
    "lat": [
        32.8,64.8,34.0,34.8,37.3,39.0,41.6,39.0,28.6,32.6,21.1,44.1,40.0,40.3,42.0,38.5,37.5,31.0,45.3,
        39.0,42.3,44.8,46.3,32.7,38.5,47.0,41.5,38.5,43.2,40.1,34.4,43.0,35.5,47.5,40.4,35.5,44.0,41.2,
        41.7,33.8,44.5,35.5,32,40.0,44.0,37.5,47.4,38.6,45.0,43.0
    ],
    
    # Longitud
    "lon": [
        -86.8,-152.4,-111.1,-92.4,-119.7,-105.5,-72.7,-75.5,-82.4,-83.4,-157.5,-114.1,-89.0,-86.1,-93.5,
        -98.0,-85.0,-92.0,-69.0,-76.7,-71.8,-84.6,-94.0,-89.7,-92.6,-110.0,-99.8,-117.0,-71.6,-74.7,
        -106.0,-75.0,-79.0,-100.0,-82.8,-97.5,-120.5,-77.2,-71.5,-80.9,-100.0,-86.6,-99.9,-111.9,-72.7,
        -77.9,-120.7,-81.0, -89.5, -107.5
    ],
    
    # Votos Trump
    "trump": [
        1318255,163387,1252401,684872,4483810,1202484,673215,185127,4617886,
        2089104,128847,409055,2146015,1557286,800983,671018,1202971,1178638,335593,
        943169,1090893,2279543,1322951,700714,1594511,279240,495961,512058,345790,
        1601933,319667,2819534,2362631,216794,2841005,949136,782403,2970733,180543,
        1155389,227721,1522925,4685047,515231,95369,1769443,1584658,489371,1405284,174419
    ],

    # Votos Clinton
    "clinton": [
        729547,116454,1161167,380494,8753788,1338870,897572,235603,4504975,
        1877963,266891,189765,3090729,1033126,653669,427005,628854,780154,357735,
        1677928,1995196,2268839,1367716,462201,1071068,177709,284494,539260,348526,
        2148278,385234,4143997,2189316,93758,2394164,420375,1002106,2926441,252525,
        855373,117442,870695,3877868,310676,178573,1981473,1742718,188794,1382536,55973
    ],

    # Votos Otros
    "otros": [
        26451,18725,106327,30069,546334,208962,62980,15027,297951,
        126849,30271,61169,310902,144972,112461,87612,62889,74463,59565,
        112957,176460,250902,254356,29215,118695,59418,74434,80094,38165,
        115943,92395,379606,192772,21565,174498,83181,191985,266208,21765,
        49287,37984,104949,283492,283738,30071,233715,223360,30394,188330,25510
    ]
}

for key, value in data.items():
    print(key, len(value))

df = pd.DataFrame(data)

# Total votes
df["total_votes"] = df["trump"] + df["clinton"] + df["otros"]
color_map = {
    "Trump": "red",
    "Clinton": "blue",
    "Otros": "gray"
}

# Color del ganador
def ganador(row):
    if row["trump"] > row["clinton"] and row["trump"] > row["otros"]:
        return "Trump"
    elif row["clinton"] > row["trump"] and row["clinton"] > row["otros"]:
        return "Clinton"
    else:
        return "Otros"

df["Ganador"] = df.apply(ganador, axis=1)
df["id"] = df.index
df["pct_trump"] = df["trump"] / df["total_votes"] * 100
df["pct_clinton"] = df["clinton"] / df["total_votes"] * 100
df["pct_otros"] = df["otros"] / df["total_votes"] * 100
df = df.reset_index(drop=True)

# Mapa
fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="total_votes",
    color="Ganador",
    projection="albers usa",
    size_max=60,
    color_discrete_map={
        "Trump": "red",
        "Clinton": "blue",
        "Otros": "gray"
    }
)

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="total_votes",
    color="Ganador",
    projection="albers usa",
    size_max=60,
    color_discrete_map={
        "Trump": "red",
        "Clinton": "blue",
        "Otros": "gray"
    },
    custom_data=["id", "state", "total_votes", "trump", "clinton",
                 "otros", "pct_trump", "pct_clinton", "pct_otros", "Ganador"]
)

fig.update_traces(
    hovertemplate=(
        "<b>%{customdata[1]}</b><br><br>"
        "Total de votos = %{customdata[2]:,}<br>"
        "Votos a Trump = %{customdata[3]:,} (%{customdata[6]:.1f}%)<br>"
        "Votos a Clinton = %{customdata[4]:,} (%{customdata[7]:.1f}%)<br>"
        "Votos a Otros = %{customdata[5]:,} (%{customdata[8]:.1f}%)<br><br>"
        "Ganador = %{customdata[9]}<extra></extra>"
    )
)

fig.add_annotation(
    text=(
        'Fuentes:<br>'
        '<a href="https://en.wikipedia.org/wiki/2016_United_States_presidential_election" '
        'style="color:lightgray;">2016 United States presidential election</a>'
    ),
    xref="paper", yref="paper",
    x=0, y=1.07,
    showarrow=False,
    font=dict(size=12, color="gray"),
    align="left"
)

fig.update_layout(
    title="<b>Elecciones de Estados Unidos 2016</b>",
    geo=dict(
        scope="usa",
        bgcolor="#111",        
        lakecolor="#111",      
        landcolor="#222",      
        subunitcolor="white",  
        showlakes=False,
        showland=True
    ),
    margin=dict(t=120),
    paper_bgcolor="#111",      
    plot_bgcolor="#111",       
    font=dict(color="white")   
)

html = fig.to_html(include_plotlyjs="cdn", full_html=True)
with open("proportional_map.html", "w", encoding="utf-8") as f:
    f.write(html)
