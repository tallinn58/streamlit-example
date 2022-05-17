from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("Kac Yasindasin")
dogum=st.number_input("Dogum Tarihiniz")
yas=2022-dogum
st.subheader(yas)
