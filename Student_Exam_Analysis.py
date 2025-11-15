import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr


def preprocessing(df):
    """
    Preprocess the data by showing summary statistics and missing values.
    """
    print("Data Summary:")
    print(df.describe())
    print("\nMissing Values:\n", df.isnull().sum())
    return df


def statistical_analysis(df, col: str):
    """
    Calculates mean, standard deviation, skewness, and kurtosis for a column.
    """
    mean = df[col].mean()
    std_dev = df[col].std()
    skewness = df[col].skew()
    kurtosis = df[col].kurt()
    return mean, std_dev, skewness, kurtosis


def plot_relational_plot(df):
    """
    Scatter plot of math vs reading scores with trend line.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='math score', y='reading score', hue='gender', data=df)
    sns.regplot(
        x='math score',
        y='reading score',
        data=df,
        scatter=False,
        color='black'
    )

    # Correlation coefficient
    corr, _ = pearsonr(df['math score'], df['reading score'])
    plt.text(30, 100, f'Corr = {corr:.2f}', fontsize=20, color='black')

    plt.title('Math Score vs Reading Score by Gender', fontsize=20)
    plt.xlabel('Math Score', fontsize=20)
    plt.ylabel('Reading Score', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=16)
    plt.grid(True)
    plt.savefig('relational_plot.png', bbox_inches='tight')
    plt.show()
    return


def plot_categorical_plot(df):
    """
    Bar plot of average writing score by test preparation.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x='test preparation course',
        y='writing score',
        data=df,
        estimator=np.mean,
    )
    plt.title('Average Writing Score by Test Preparation Course', fontsize=20)
    plt.xlabel('Test Preparation Course', fontsize=20)
    plt.ylabel('Average Writing Score', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig('categorical_plot.png', bbox_inches='tight')
    plt.show()
    return


def plot_statistical_plot(df):
    """
    Correlation heatmap and histogram of math scores with mean line.
    """
    # Correlation heatmap
    plt.figure(figsize=(10, 6))
    numeric_cols = ['math score', 'reading score', 'writing score']
    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap='coolwarm',
        fmt='.2f',
        linewidths=0.5
    )
    plt.title('Correlation Heatmap of Exam Scores', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=16)
    plt.savefig('statistical_heatmap.png', bbox_inches='tight')
    plt.show()

    # Histogram of math scores with mean line
    plt.figure(figsize=(10, 6))
    sns.histplot(df['math score'], bins=10, kde=True, color='skyblue')
    mean = df['math score'].mean()
    plt.axvline(mean, color='red', linestyle='--', label=f'Mean = {mean:.2f}')
    plt.title('Distribution of Math Scores', fontsize=20)
    plt.xlabel('Math Score', fontsize=20)
    plt.ylabel('Frequency', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=20)
    plt.savefig('math_score_histogram.png', bbox_inches='tight')
    plt.show()
    return


def writing(moments, col):
    """
    Prints four key statistical moments,interprets skewness & kurtosis.
    """
    print(f'\nStatistics for "{col}":')
    print(f'Mean = {moments[0]:.2f}')
    print(f'Standard Deviation = {moments[1]:.2f}')
    print(f'Skewness = {moments[2]:.2f}')
    print(f'Excess Kurtosis = {moments[3]:.2f}')
    # Interpret skewness
    if moments[2] > 0:
        skew_text = "right-skewed"
    elif moments[2] < 0:
        skew_text = "left-skewed"
    else:
        skew_text = "symmetrical"
    # Interpret kurtosis
    if moments[3] > 0:
        kurt_text = "leptokurtic (peaked)"
    elif moments[3] < 0:
        kurt_text = "platykurtic (flat)"
    else:
        kurt_text = "mesokurtic (normal-shaped)"

    print(f"The distribution is {skew_text} and {kurt_text}.")
    return


def main():
    """
    Main workflow: load data, preprocess, create plots, calculate statistics.
    """
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'math score'

    plot_relational_plot(df)
    plot_categorical_plot(df)
    plot_statistical_plot(df)

    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
    