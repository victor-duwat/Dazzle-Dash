from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Charger les données
df = pd.read_csv('LifeExpectancyData.csv')
df_life_expectancy_bmi = pd.read_csv('life_expectancy_bmi.csv')
df_thinness_schooling = pd.read_csv('Thinness _1-19_years_schooling.csv')

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

fig3 = px.scatter(
    df, 
    x='Income composition of resources', 
    y='Schooling', 
    title="Correlation with Regression Line between Income composition of resources and Schooling",
    labels={'Income composition of resources': 'Income composition of resources', 'Schooling': 'Schooling'},
    trendline="ols",  # Ajouter une ligne de régression ordinaire (OLS)
    trendline_color_override='red'  # Définir la couleur de la ligne de régression en rouge
)
fig3.update_traces(marker=dict(opacity=0.6))

fig4 = px.scatter(
    df, 
    x='Life expectancy ', 
    y='Schooling', 
    title="Correlation with Regression Line between Life expectancy and Schooling",
    labels={'Life expectancy ': 'Life expectancy ', 'Schooling': 'Schooling'},
    trendline="ols",  # Ajouter une ligne de régression ordinaire (OLS)
    trendline_color_override='red'  # Définir la couleur de la ligne de régression en rouge
)
fig4.update_traces(marker=dict(opacity=0.6))

fig5 = px.line(
    df_thinness_schooling,
    x='Year',
    y=[' thinness  1-19 years', 'Schooling'],
    labels={'value': 'Value', 'variable': 'Indicator'},
    title='Evolution of  thinness  1-19 years and schooling over the Years',
)
fig5.update_traces(mode='lines+markers')
fig5.update_layout(template='plotly_white')

# Initialiser l'application Dash
app = Dash()

# Ajouter les deux graphiques dans le layout de Dash
app.layout = html.Div([
    html.H1("Life Expectancy Data Dashboard"),
    
    # Conteneur pour centrer les graphiques
    html.Div([
        # Premier graphique (Life Expectancy et BMI)
        html.Div([
            dcc.Graph(id='life-expectancy-bmi-graph', figure=fig1)
        ], style={'width': '80%'}),
        
        # Deuxième graphique (Régression entre Life Expectancy et Adult Mortality)
        html.Div([
            dcc.Graph(id='life-expectancy-mortality-graph', figure=fig2)
        ], style={'width': '80%'}),
        html.Div([
            dcc.Graph(id='thinness-schooling-graph', figure=fig5)
        ], style={'width': '80%'}),
        html.Div([
            dcc.Graph(id='Income-composition-of-ressources-graph', figure=fig3)
        ], style={'width': '80%'}),
        html.Div([
            dcc.Graph(id='life-expectancy-schooling-graph', figure=fig4)
        ], style={'width': '80%'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'flex-direction': 'column', 'align-items': 'center'})
])

if __name__ == '__main__':
    app.run_server()