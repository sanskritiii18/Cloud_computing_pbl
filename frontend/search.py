import requests
import streamlit as st


def searching():
    query = st.text_input("Enter song name")
    if query:
        try:
            response = requests.get("http://localhost:5050/search", params={"query": query})
            response.raise_for_status()
            songs = response.json()


            if not songs:
                st.warning("No songs found for this query.")
            else:
                for song in songs:
                    st.subheader(song['title'])
                    st.image(song['image_url'])
                    st.audio(song['url'], format='audio/mp3')


        except requests.RequestException as e:
            st.error(f"Request failed: {e}")
