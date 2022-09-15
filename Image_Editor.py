from turtle import width
import streamlit as st
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

st.markdown("<h1 style='text-align:center;'>Image Resizer</h1>",unsafe_allow_html=True)
st.markdown("---")
image = st.file_uploader("upload your image",type=['jpg','png','jpeg'])
st.markdown("<h2 style='text-align:center;'>Image Info</h2>",unsafe_allow_html=True)
size = st.empty()
mode = st.empty()
format = st.empty()
if image:
 img = Image.open(image) 
 st.image(img)
 size.markdown(f"<h6>size: {img.size}</h6",unsafe_allow_html=True)
 mode.markdown(f"<h6>Mode:{img.mode}</h6>",unsafe_allow_html=True)
 format.markdown(f"<h6>format:{img.format}</h6>",unsafe_allow_html=True)

 
 st.markdown("<h2 style='text-align:center;'>Resize</h2>",unsafe_allow_html=True)

 Width = st.number_input("Width",value = img.width)
 Height = st.number_input("Height",value = img.height)
 st.markdown("---")
 st.markdown("<h2 style='text-align:center;'>Rotate Image</h2>",unsafe_allow_html=True)
 rotate= st.number_input("rotate")
 st.markdown("---")

 st.markdown("<h2 style='text-align:center;'>Edit Image</h2>",unsafe_allow_html=True)
 filter= st.selectbox("Select the effect",['None','Blur','CONTOUR','EDGE_ENHANCE','SMOOTH','SHARPEN'])
 btn = st.button("Submit")
 if btn:
    x= img.resize((Width,Height)).rotate(rotate)
    filtered = x
    if filter !='None':
      filtered = x.filter(ImageFilter.BLUR)
    elif filter == 'CONTOUR':
      filtered = x.filter(ImageFilter.CONTOUR)
    elif filter == 'EDGE_ENHANCE':
      filtered = x.filter(ImageFilter.EDGE_ENHANCE)
    elif filter == 'SMOOTH':
      filtered = x.filter(ImageFilter.SMOOTH)
    elif filter == 'SHARPEN':
      filtered = x.filter(ImageFilter.SHARPEN)
    st.image(filtered)


