import streamlit as st
from frontend.search import searching


def show_home():
    st.title("Welcome to Suno 🎵")
    #st.write("Enjoy unlimited music streaming!")

    st.sidebar.header("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Your Playlists", "Search Songs", "Settings"])

    if selection == "Home":
        st.subheader("🎧 Featured Tracks")
        
    elif selection == "Your Playlists":
        st.subheader("🎶 Your Playlists")
        st.info("Feature coming soon!")
    elif selection == "Search Songs":
        st.subheader("🔍 Search Songs")
        searching()
    elif selection == "Settings":
        st.subheader("⚙️ Settings")
        st.info("Settings coming soon!")






# 🔥 Prevent automatic execution when imported into `main.py`
if __name__ == "__main__":
    show_home()
