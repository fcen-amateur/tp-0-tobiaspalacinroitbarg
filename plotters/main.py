import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(gapminder[["continent", "gdpPercap"]].drop_duplicates(), x="continent")
        .add(so.Bar(), so.Hist())
        .label(
            title="PBI Per Cápita por Continente",
            x="Continente",
            y="PBI Pér Cápita",
        )
    )
    return dict(
        descripcion="Un sofisticado gráfico con el número de países en cada continente",
        autor="Tobías Palacín Roitbarg LU: 6/23",
        figura=figura,
    )
