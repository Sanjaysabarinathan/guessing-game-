import streamlit as st
import random

st.title("Guessing Game")
mode = st.radio("Mode:", ["User Guesses", "Machine Guesses"])

if mode == "User Guesses":
    target = st.session_state.get("target", random.randint(1, 100))
    guess = st.number_input("Your guess:", 1, 100)
    if st.button("Check"):
        st.write("Too low!" if guess < target else "Too high!" if guess > target else "Correct!")
        if guess == target: st.session_state.target = random.randint(1, 100)

else:
    target = st.slider("Pick a number for the machine:", 1, 100)
    guess = (st.session_state.get("low", 1) + st.session_state.get("high", 100)) // 2
    st.write(f"Machine guesses: {guess}")
    if st.button("Too Low"): st.session_state["low"] = guess + 1
    elif st.button("Too High"): st.session_state["high"] = guess - 1
    elif st.button("Correct"): st.write("Machine guessed it!"); st.session_state.clear()
