import streamlit as st
import pandas as pd
import seaborn as sns


#make container

header = st.container()
data_set = st.container()
features = st.container()
model_training = st.container()

with header:
     st.title('kashti ki app')
     st.text('in the project we will work on kashti ki app')

with data_set:
    st.header("kashti doob gaye, Haww")
    st.text("we will work on data set")
    # import data
    df = sns.load_dataset("titanic")
    st.write(df.head(10))
    st.subheader("sex distribution")
    st.bar_chart(df["sex"].value_counts())
    st.subheader("class distribution")
    st.bar_chart(df["class"].value_counts())
    st.subheader("age distribution")
    st.bar_chart(df['age'].sample(10))
   

with features:
    st.header("kuch features")
    st.text("we will work on features")
    st.markdown("1. **Features 1:** This is first feature") 
    st.markdown("2. **Features 2:** This is second feature")
    st.markdown("3. **Features 3:** This is third feature")

with model_training:
    st.header("model training")
    st.text("we will work on model training")
    # making colums
    input, display = st.columns(2)
    input.slider("How many people do you know?", min_value=10, max_value=100, value=20, step=5)

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
df1 = px.data.gapminder()
df1.head(10)
df1['year'].unique()