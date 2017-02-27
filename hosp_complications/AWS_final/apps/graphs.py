import plotly.plotly as py
import plotly.tools as tls
import plotly.utils
import json
tls.set_credentials_file(username='sheenas',api_key='618CQEhf8rlkmtYhNYi5')

with gzip.open('test.dill.gz', 'r') as gg:
   test = dill.load(gg)


data = [ dict(
        type='choropleth',
      #  colorscale = scl,
        autocolorscale = True,
        locations = test['states'],
        z = test['aves'].astype(float),
        locationmode = 'USA-states',
        text = test['text'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Readmissions Rate")
        ) ]

layout = dict(
        title = 'Risk Standarized Hospital Readmission Rates by State<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)',
        ),
    )

fug = dict(data=data, layout=layout)

url = py.plot(fug, filename='d3-cloropleth-map')

graphJSON = json.dumps(fug, cls=plotly.utils.PlotlyJSONEncoder)
