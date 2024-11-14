from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Charger les données
df = pd.read_csv('LifeExpectancyData.csv')
df_life_expectancy_bmi = pd.read_csv('life_expectancy_bmi.csv')

# Créer le graphique avec Plotly Express
fig1 = px.line(
    df_life_expectancy_bmi,
    x='Year',
    y=['Life expectancy ', ' BMI '],
    labels={'value': 'Value', 'variable': 'Indicator'},
    title='Evolution of Life Expectancy and BMI over the Years',
)
fig1.update_traces(mode='lines+markers')
fig1.update_layout(template='plotly_white')

# Créer le deuxième graphique avec Plotly Express (Régression entre Life Expectancy et Adult Mortality)
fig2 = px.scatter(
    df, 
    x='Life expectancy ', 
    y='Adult Mortality', 
    title="Correlation with Regression Line between Life Expectancy and Adult Mortality",
    labels={'Life expectancy ': 'Life Expectancy', 'Adult Mortality': 'Adult Mortality'},
    trendline="ols",  # Ajouter une ligne de régression ordinaire (OLS)
    trendline_color_override='red'  # Définir la couleur de la ligne de régression en rouge
)
fig2.update_traces(marker=dict(opacity=0.6))  # Modifier la transparence des points

# Initialiser l'application Dash
app = Dash()

# Ajouter les deux graphiques dans le layout de Dash (en les plaçant sous forme de colonnes)
app.layout = html.Div([
    html.H1("Life Expectancy and BMI Dashboard"),
    
    # Premier graphique (Life Expectancy et BMI)
    html.Div([
        dcc.Graph(id='life-expectancy-bmi-graph', figure=fig1)
    ], style={'width': '48%', 'display': 'inline-block'}),
    
    # Deuxième graphique (Régression entre Life Expectancy et Adult Mortality)
    html.Div([
        dcc.Graph(id='life-expectancy-mortality-graph', figure=fig2)
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
])

if __name__ == '__main__':
    app.run_server()