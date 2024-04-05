import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

def convert_to_xml(df: pd.DataFrame):
    xml_data = df.to_xml()
    return xml_data


def visulaize_data(df: pd.DataFrame):
    fig, axs = plt.subplots(1, 2)  
    axs[0].plot()
    category_counts = df['Category'].value_counts()
    axs[0].bar(category_counts.index, height=category_counts.values, color='orange', edgecolor='black', linewidth=1.2)
    axs[0].set_title('API Categories')
    axs[0].set_xlabel('Category')
    axs[0].set_ylabel('Count')
    axs[0].set_xticks(category_counts.index) 
    axs[0].set_xticklabels(category_counts.index, rotation=90, fontsize=8) 

    auth_counts = df['Auth'].value_counts()
    axs[1].pie(auth_counts, autopct='%1.1f%%', startangle=90)
    axs[1].set_title('API Authentication')
    auth_counts.index = auth_counts.index.fillna('No API Auth')
    legend_labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(auth_counts.index, 100*auth_counts/auth_counts.sum())]
    axs[1].legend(legend_labels, title="Auth Types", bbox_to_anchor=(1,1), loc="upper left")  
    plt.suptitle('API Data')
    mplcursors.cursor(hover=True)
    plt.tight_layout( rect=[0, 0.03, 1, 0.95])
    plt.show()

url = "https://api.publicapis.org/entries"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # print(data["entries"])
    df = pd.DataFrame(data["entries"])
    category_counts = df['Category'].value_counts()
    xml_data = convert_to_xml(df)
    print(xml_data)
    print(df.head())
    visulaize_data(df)

else:
    print("Error:", response.status_code)

