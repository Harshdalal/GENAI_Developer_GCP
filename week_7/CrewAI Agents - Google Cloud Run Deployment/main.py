import streamlit as st
import os
from agents import research_agent, blog_team

# Simple page setup
st.set_page_config(page_title="AI Agents", page_icon="🤖")

# Title
st.title("🤖 AI Agents")
st.write("Use AI agents to research topics or create blog posts")

# Get API key
st.sidebar.header("Setup")
st.sidebar.success("API Key Ready!")

# Choose what to do
option = st.radio("What do you want to do?", 
                  ["Research a topic", "Create a blog post"])

if option == "Research a topic":
    st.header("Research Agent")
    
    topic = st.text_input("What topic do you want to research?", 
                         value="Benefits of AI")
    
    if st.button("Start Research"):
        if topic:
            with st.spinner("Researching..."):
                try:
                    result = research_agent(topic)
                    st.success("Done!")
                    st.write(result)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a topic")

else:  # Create blog post
    st.header("Blog Creation Team")
    
    topic = st.text_input("What should the blog post be about?", 
                         value="Future of remote work")
    
    if st.button("Create Blog Post"):
        if topic:
            with st.spinner("Creating blog post..."):
                try:
                    result = blog_team(topic)
                    st.success("Done!")
                    st.write(result)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a topic")