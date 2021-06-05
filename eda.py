import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("titanics_Dataset")
#import dataset
df = pd.read_csv('titanics.csv')
#First thirty rows
titanics = df.head(10)
#Display the table
st.table(titanics)
#############
#bar plot
st.subheader("Bar Plot")
titanics.plot(kind='bar')
st.pyplot()
################
#pairplot
st.subheader("Pairplot")
sns.pairplot(titanics,hue='Sex',palette='rainbow')
st.pyplot()
######################