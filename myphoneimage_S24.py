import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import io
from rembg import remove

# CSV 파일 불러오기
@st.cache_data
def load_data():
    file_path = "age2411.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

# 지역 목록 추출
df["\ud589\uc815\uad6c\uc5ed"] = df["\ud589\uc815\uad6c\uc5ed"].str.split(" ").str[-1]  # \ud589\uc815\uad6c\uc5ed\uc5d0\uc11c \ub9c8\uc9c0\ub9c8 \ub2e4\ub974\uac8c \uacb0\ud569
octlmar doc update completion
