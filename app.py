import streamlit as st
import pickle
from datetime import datetime
# startTime = datetime.now()
# import znanych nam bibliotek

# objawy	wiek	choroby	wzrost	zdrowie
# 1		0	170	0
# 1	65	0		0
# 1	55	0	182	0
# 1	44	0	187	0
# 1	77	0	165	0
# 1	64	0	164	0
# 2	54	1	178	0
# 1		1	190	0
# 1	76	1	200	0
# 2	54	0	198	0
# 3	56	0	187	0
# 1	68	0	167	0
# 3		1	168	0
# 2	55	1	189	0

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
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
		st.header("Czy wyzdrowiejesz po tygodniu? {0}".format("Tak" if survival[0] == 1 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
