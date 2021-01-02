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
    # Cleaning the data so no erroneous or outliers patients are included
    df_heat = df[(df.ap_lo <= df.ap_hi) &
                 (df.height >= df.height.quantile(0.025)) &
                 (df.height <= df.height.quantile(0.975)) &
                 (df.weight >= df.weight.quantile(0.025)) &
                 (df.weight <= df.weight.quantile(0.975))]

    # Establishing the correlation matrix
    corr = df_heat.corr()

    # Generating a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, square=True, annot=True, fmt=".1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
