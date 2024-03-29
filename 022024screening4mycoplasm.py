import pickle
import streamlit as st
model=pickle.load(open("bestmycoplasme.pickle","rb"))
st.title("Screenig4Mycoplasma Application: a Machine Learning approach")

building=st.selectbox("Building ID",["1","2","3","4","5","6"])

mortality=st.text_input("Number of dead Chicken (s)",value=0)

staffing=st.text_input("Staffing Levels in Place",value=0)

age=st.text_input("Chicken Age",value=0)

ftype=st.selectbox("Feed Type",["1","2","3"])

fquantity=st.text_input("Feed Quantity (Kg)",value=0.0)

waterconsumption=st.text_input("Water Consumption (L)",value=0.0)

maxt=st.text_input("Maximum Tempreature (C°)",value=0.0)

mint=st.text_input("Minimum Temperature (C°)",value=0.0)

lighting=st.text_input("Lighting (Hours)",value=0.0)

maxh=st.text_input("Maximum Humidity (%)",value=0.0)

minh=st.text_input("Minimum Humidity (%)",value=0.0)

strain=st.selectbox("Chicken Strain",["1","2"])

season=st.selectbox("Season",["Winter","Spring","Summer","Autumn"])
if season=="Winter":
  season=1
elif season=="Spring":
  season=2
elif season=="Summer":
  season=3
else:
  season=4
features=[[int(building),mortality,staffing,age,int(ftype),fquantity,waterconsumption,maxt,mint,lighting,maxh,minh,int(strain),season]]
pred=model.predict(features)
if st.button("Screenig4Mycoplasma Check"):
  if pred==0:
    st.success("No Mycoplasma")
  else:
    st.success("Presence of Mycoplasma")
