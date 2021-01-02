import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = ((df["weight"]/(df["height"]/100)**2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad.
df.loc[(df.cholesterol == 1), 'cholesterol'] = 0
df.loc[(df.cholesterol > 1), 'cholesterol'] = 1
df.loc[(df.gluc == 1), 'gluc'] = 0
df.loc[(df.gluc > 1), 'gluc'] = 1


def draw_cat_plot():
    # Create DataFrame for cat plot.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'.
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['variable', 'cardio', 'value'], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', y='total', hue="value", col="cardio", data=df_cat, kind='bar')
    fig = g.fig

    # Save the file
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
