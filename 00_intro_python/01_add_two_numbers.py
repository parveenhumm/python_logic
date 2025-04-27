import streamlit as st

st.title("➕Adding two Numbers")

def main():
 col1, col2 = st.columns(2)
 with col1:
   num_01 = st.number_input("🔢 Enter First Number:")
   num_1= int(num_01)

 with col2:
   num_02 = st.number_input("🔢 Enter Second Number:")
   num_2 = int(num_02) 

 cola, colb, colc = st.columns(3)
 with colb:
     if st.button("📱 Calculate Sum"):
      add = num_1 + num_2
      st.success(f"By adding {+num_1} and {num_2} is: {add}")
      st.balloons()

if __name__ == "__main__":
 main()
