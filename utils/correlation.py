import seaborn as sns
import matplotlib.pyplot as plt

def checkcor(data):
    corr = data.corr()
    plt.figure(figsize=(5,5))
    sns.heatmap(corr, annot=True)
    plt.title("Korelasi Data Performance Students")

