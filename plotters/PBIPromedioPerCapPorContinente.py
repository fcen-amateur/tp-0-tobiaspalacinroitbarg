import seaborn.objects as so
from gapminder import gapminder

avg_gdp_per_capita = gapminder.groupby('continent')['gdpPercap'].mean().reset_index()

def plot():
    figura = (
   
        so.Plot(data=avg_gdp_per_capita, x="continent",y="gdpPercap")
        .add(so.Bar())
        .label(
            title="Promedio Histórico de PBI Per Cápita por Continente",
            x="Continente",
            y="PBI Pér Cápita",
        )
    )
    return dict(
        descripcion="Un sofisticado gráfico con el PBI per cápita promedio de cada continente a lo largo de la historia",
        autor="Tobías Palacín Roitbarg LU: 6/23",
        figura=figura,
    )
