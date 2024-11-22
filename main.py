import random
import streamlit as st

# Game logic function
def play_game(user_choice):
    options = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}
    computer_choice = random.choice([1, -1, 0])

    user_display = options[user_choice]
    computer_display = options[computer_choice]

    if user_choice == computer_choice:
        return f"You chose {user_display}, Computer chose {computer_display}. It's a draw!"
    elif (user_choice == 1 and computer_choice == -1) or \
         (user_choice == -1 and computer_choice == 0) or \
         (user_choice == 0 and computer_choice == 1):
        return f"You chose {user_display}, Computer chose {computer_display}. 🎉 You win!"
    else:
        return f"You chose {user_display}, Computer chose {computer_display}. 😔 You lose!"

# Main function for the Streamlit UI
def main():
    # Initialize session state for results
    if "result" not in st.session_state:
        st.session_state.result = ""

    # Title with emoji
    st.markdown("# 🐍💧🔫 Snake-Water-Gun Game")
    st.write("Make your choice and see if you can beat the computer!")


    # Buttons with emojis for user choices
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🐍 Snake"):
            st.session_state.result = play_game(1)
    with col2:
        if st.button("💧 Water"):
            st.session_state.result = play_game(-1)
    with col3:
        if st.button("🔫 Gun"):
            st.session_state.result = play_game(0)

    # Display the result with a card-like effect
    if st.session_state.result:
        st.markdown(f"""
        <div style="background-color: ; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
            <h3>{st.session_state.result}</h3>
        </div>
        """, unsafe_allow_html=True)

    # Play again button with a fresh look
    if st.button("🔄 Play Again"):
        st.session_state.result = ""  # Reset the result to play again

    # Add footer with styling
    st.markdown("""
    <hr>
    <div style="text-align: center; font-size: 14px; color: #888;">
        Created with ❤️ Ayush jain
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
