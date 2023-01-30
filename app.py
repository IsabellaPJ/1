import pickle
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
st.set_option('deprecation.showPyplotGlobalUse', False)

model=pickle.load(open("rfc.pkl", "rb"))

def main():
    # Sidebar    
    st.title("Mushroom Classification")  
    shape=st.selectbox("Cap Shape",['x', 'b', 's', 'f', 'k', 'c'])
    surface=st.selectbox("Cap Surface",['s', 'y', 'f', 'g'])
    color=st.selectbox("Cap color",['n', 'y', 'w', 'g', 'e', 'p', 'b', 'u', 'c', 'r'])
    bruises=st.selectbox("Bruises",['t', 'f'])
    odor=st.selectbox("Odor",['p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm'])
    gattachment=st.selectbox("Gill Attachment",['f', 'a'])
    gspacing=st.selectbox("Gill Spacing",['c', 'w'])
    gsize=st.selectbox("Gill Size",['n', 'b'])
    gcolor=st.selectbox("Gill Color",['k', 'n', 'g', 'p', 'w', 'h', 'u', 'e', 'b', 'r', 'y', 'o'])
    sshape=st.selectbox("Stalk Shape",['e', 't'])
    sroot=st.selectbox("Stalk Root",['e', 'c', 'b', 'r', '?'])
    ssurabovering=st.selectbox("Stalk Surface Above Ring",['s', 'f', 'k', 'y'])
    ssurbelowring=st.selectbox("Stalk Surface Below Ring",['s', 'f', 'y', 'k'])
    scolabovering=st.selectbox("Stalk Color Above Ring",['w', 'g', 'p', 'n', 'b', 'e', 'o', 'c', 'y'])
    scolbelowring=st.selectbox("Stalk Color Below Ring",['w', 'p', 'g', 'b', 'n', 'e', 'y', 'o', 'c'])
    vtype=st.selectbox("Veil Type",['p'])
    vcolor=st.selectbox("Veil Color",['w', 'n', 'o', 'y'])
    ringnum=st.selectbox("Ring Number",['o', 't', 'n'])
    ringtyp=st.selectbox("Ring Type",['p', 'e', 'l', 'f', 'n'])
    spricolor=st.selectbox("Spore Print Color",['k', 'n', 'u', 'h', 'w', 'r', 'o', 'y', 'b'])
    population=st.selectbox("Population",['s', 'n', 'a', 'v', 'y', 'c'])
    habitat=st.selectbox("Habitat",['u', 'g', 'm', 'd', 'p', 'w', 'l'])
    df = pd.DataFrame(data=[[shape,surface,color,bruises,odor,gattachment,gspacing, gsize, gcolor, sshape, sroot, ssurabovering, ssurbelowring, scolabovering, scolbelowring, vcolor, ringnum, ringtyp, spricolor, population, habitat]], 
                      columns=['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-color', 'ring-number', 'ring-type',
       'spore-print-color', 'population', 'habitat'])

    if st.button("Analyze"):
        prediction = model.predict(df)
        if prediction == 0:
            st.success("Edible")
        else:
            st.error("Poisonous")
   

def load_data():
    df = pd.read_csv("HR_Dataset.csv")
    return df 

if __name__ == "__main__":
    main()