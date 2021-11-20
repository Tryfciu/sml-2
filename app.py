import streamlit as st
import pickle
from datetime import datetime

filename = "model.sv"
model = pickle.load(open(filename,'rb'))

def main():
	st.set_page_config(page_title="Czy wyzdrowiejesz po tygodniu?")
	overview = st.container()
	prediction = st.container()

	st.image("https://th.bing.com/th/id/OIP.7MLzt5CWxJU0iekQo5u0ogHaEK?pid=ImgDet&rs=1")

	with overview:
		st.title("Czy wyzdrowiejesz po tygodniu?")
		symptoms_amount = st.slider("Ilość objawów", value=1, min_value=1, max_value=5)
		age = st.slider( "Wiek", value=1, min_value=1, max_value=77)
		ilnesses_amount = st.slider("Ilość chorób", value=0, min_value=0, max_value=5)
		height = st.slider( "Wzrost", value=159, min_value=159, max_value=200)

	data = [[symptoms_amount, age,  ilnesses_amount, height]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy wyzdrowiejesz po tygodniu? {0}".format("Tak" if survival[0] == 0 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
