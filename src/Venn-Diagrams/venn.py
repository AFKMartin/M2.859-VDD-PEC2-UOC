import plotly.graph_objects as go
# Fuentes:
# https://github.blog/news-insights/octoverse/octoverse-2024/
# https://survey.stackoverflow.co/2024/technology#most-popular-technologies-language
# https://www.jetbrains.com/lp/devecosystem-2024/
# Datos

SO = {
    "JavaScript",
    "HTML/CSS",
    "Python",
    "SQL",
    "TypeScript",
    "Shell",
    "Java",
    "C#",
    "C++",
    "C",
    "PHP",
    "PowerShell",
    "Go",
    "Rust",
    "Kotlin",
    "Lua"
}

GH = {
    "Python",
    "JavaScript",
    "TypeScript",
    "Java",
    "C#",
    "C++",
    "PHP",
    "Shell",
    "C",
    "Go",
}

JB = {
    "JavaScript",
    "Python",
    "HTML/CSS",
    "SQL",
    "Java",
    "TypeScript",
    "Shell",
    "C++",
    "C#",
    "C",
    "Go",
    "PHP",
    "Kotlin",
    "Rust",
    "Dart",
    "Swift",
    "Lua",
    "Ruby",
    "Scala",
    "Objective-C"
}

only_GH = GH - JB - SO
only_JB = JB - GH - SO
only_SO = SO - GH - JB

GH_JB = (GH & JB) - SO
GH_SO = (GH & SO) - JB
JB_SO = (JB & SO) - GH

all_three = GH & JB & SO

def fmt(s):
    return "<br>".join(sorted(s)) if s else "Ninguno"

# Centros de los círculos
cx_GH, cy_GH = -1.0, 0.0
cx_JB, cy_JB =  1.0, 0.0
cx_SO, cy_SO =  0.0, 1.2
r = 2.0

shapes = [
    # GitHub
    dict(
        type="circle",
        xref="x", yref="y",
        x0=cx_GH - r, y0=cy_GH - r,
        x1=cx_GH + r, y1=cy_GH + r,
        line=dict(color="rgba(0, 150, 255, 0.8)", width=2),
        fillcolor="rgba(0, 150, 255, 0.15)"
    ),
    # JetBrains
    dict(
        type="circle",
        xref="x", yref="y",
        x0=cx_JB - r, y0=cy_JB - r,
        x1=cx_JB + r, y1=cy_JB + r,
        line=dict(color="rgba(0, 200, 0, 0.8)", width=2),
        fillcolor="rgba(0, 200, 0, 0.15)"
    ),
    # StackOverflow
    dict(
        type="circle",
        xref="x", yref="y",
        x0=cx_SO - r, y0=cy_SO - r,
        x1=cx_SO + r, y1=cy_SO + r,
        line=dict(color="rgba(255, 120, 0, 0.8)", width=2),
        fillcolor="rgba(255, 120, 0, 0.15)"
    ),
]

# hover por región
regions = [
    # Solo GitHub
    ("Solo GitHub", cx_GH - 0.6, cy_GH - 0.3, only_GH,
     "Lenguajes solo de GitHub"),

    # Solo JetBrains
    ("Solo JetBrains", cx_JB + 0.6, cy_JB - 0.3, only_JB,
     "Lenguajes solo de JetBrains"),

    # Solo StackOverflow
    ("Solo StackOverflow", cx_SO, cy_SO + 0.9, only_SO,
     "Lenguajes solo de StackOverflow"),

    # GH & JB
    ("GH & JB", 0.0, cy_GH - 1, GH_JB,
     "Lenguajes comunes de GitHub y JetBrains (sin StackOverflow)"),

    # GH & SO
    ("GH & SO", cx_GH - 0.1, cy_SO - 0.2, GH_SO,
     "Lenguajes comunes de GitHub y StackOverflow (sin JetBrains)"),

    # JB & SO
    ("JB & SO", cx_JB + 0.1, cy_SO - 0.2, JB_SO,
     "Lenguajes comunes de JetBrains y StackOverflow (sin GitHub)"),

    # GH & JB & SO
    ("GH & JB & SO", 0.0, 0.5, all_three,
     "Lenguajes comunes a GitHub, JetBrains y StackOverflow"),
]

scatter_traces = []
for name, x, y, s, desc in regions:
    scatter_traces.append(
        go.Scatter(
            x=[x],
            y=[y],
            mode="markers+text",
            text=[str(len(s))],
            textposition="middle center",
            marker=dict(size=30, color="rgba(0,0,0,0)"),
            hovertemplate=(
                f"<b>{name}</b><br>"
                f"{desc}:<br>"
                f"{fmt(s)}<extra></extra>"
            ),
            showlegend=False
        )
    )

# conjuntos
labels_traces = [
    # GitHub
    go.Scatter(
        x=[cx_GH - 2.2],
        y=[cy_GH + 2.2],
        mode="markers+text",
        text=["GitHub"],
        textfont=dict(size=16, color="rgba(0, 100, 200, 1)"),
        marker=dict(size=20, color="rgba(0,0,0,0)"),  # invisible
        hovertemplate=(
            "<b>Lenguajes en GitHub</b><br>" +
            "<br>".join(sorted(GH)) +
            "<extra></extra>"
        ),
        showlegend=False
    ),

    # JetBrains
    go.Scatter(
        x=[cx_JB + 2.2],
        y=[cy_JB + 2.2],
        mode="markers+text",
        text=["JetBrains"],
        textfont=dict(size=16, color="rgba(0, 150, 0, 1)"),
        marker=dict(size=20, color="rgba(0,0,0,0)"),
        hovertemplate=(
            "<b>Lenguajes en JetBrains</b><br>" +
            "<br>".join(sorted(JB)) +
            "<extra></extra>"
        ),
        showlegend=False
    ),

    # StackOverflow
    go.Scatter(
        x=[cx_SO],
        y=[cy_SO + 2.6],
        mode="markers+text",
        text=["StackOverflow"],
        textfont=dict(size=16, color="rgba(200, 100, 0, 1)"),
        marker=dict(size=20, color="rgba(0,0,0,0)"),
        hovertemplate=(
            "<b>Lenguajes en StackOverflow</b><br>" +
            "<br>".join(sorted(SO)) +
            "<extra></extra>"
        ),
        showlegend=False
    ),
]

# Figura final
fig = go.Figure(data=scatter_traces + labels_traces)

fig.update_layout(
    # template="plotly_dark",
    # paper_bgcolor="#111",
    # plot_bgcolor="#111",
    # font=dict(color="white"),
    title="<b>Lenguajes de programación más usados en GitHub, JetBrains y StackOverflow</b>",
    shapes=shapes,
    xaxis=dict(visible=False, range=[-4, 4]),
    yaxis=dict(visible=False, range=[-3, 4]),
    autosize=False,
    width=900,
    height=900,
    margin=dict(l=50, r=50, t=120, b=180)
)

fig.add_annotation(
    text=(
        'Fuentes:<br>'
        '<a href="https://github.blog/news-insights/octoverse/octoverse-2024/">Octoverse 2024</a><br>'
        '<a href="https://survey.stackoverflow.co/2024/technology#most-popular-technologies-language">StackOverflow Dev Survey 2024</a><br>'
        '<a href="https://www.jetbrains.com/lp/devecosystem-2024/">JetBrains Dev Ecosystem 2024</a>'
    ),
    xref="paper", yref="paper",
    x=0, y=-0.18,
    showarrow=False,
    font=dict(size=12, color="gray"),
    align="left"
)

html = fig.to_html(
    include_plotlyjs="cdn",
    full_html=True
)

# Cambiar fondo HTML
html = html.replace(
    "<body>",
    "<body style='background-color:#111; display:flex; justify-content:center; padding:40px;'>"
)

with open("venn.html", "w", encoding="utf-8") as f:
    f.write(html)

