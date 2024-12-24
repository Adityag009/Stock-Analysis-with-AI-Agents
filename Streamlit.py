import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import markdown

# Load environment variables
load_dotenv()

# Define agents
agents = {
    "Groq": Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), DuckDuckGo()],
        description="Investment analyst for stock prices, recommendations, and fundamentals.",
        show_tool_calls=True,
        markdown=True,
        instruction=["Use tables to display data."]
    ),
    "Gemini": Agent(
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), DuckDuckGo()],
        description="Investment analyst for stock prices, recommendations, and fundamentals.",
        show_tool_calls=True,
        markdown=True,
        instruction=["Use tables to display data."]
    ),
    "OpenAIChat": Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), DuckDuckGo()],
        description="Investment analyst for stock prices, recommendations, and fundamentals.",
        show_tool_calls=True,
        markdown=True,
        instruction=["Use tables to display data."]
    )
}

# Streamlit UI
st.title("Stock Analysis with AI Agents")

# Select model
model_choice = st.selectbox("Select AI Model", options=list(agents.keys()))
selected_agent = agents[model_choice]

# Input for stock comparison or analysis
query_type = st.radio("What would you like to do?", ["Compare Stocks", "Analyze Chart Pattern"])

if query_type == "Compare Stocks":
    stocks = st.text_input("Enter stock symbols for comparison (comma-separated, e.g., TCS, INFY):")
    if st.button("Analyze"):
        if stocks:
            query = f"Summarize and Compare analyst recommendation and fundamentals for {stocks}"
            print(stocks)
            response = selected_agent.run(query, stream=False)
            print(response)
            try:
                st.markdown(response.content)  # Use correct attribute for response
            except AttributeError:
                st.error("Unexpected response format. Check the agent configuration.")
            # else:
            #     st.error("Please enter stock symbols.")
elif query_type == "Analyze Chart Pattern":
    uploaded_file = st.file_uploader("Upload a chart image for pattern analysis", type=["png", "jpg", "jpeg"])
    if st.button("Analyze Image"):
        if uploaded_file:
            # Display the uploaded image for user confirmation
            st.image(uploaded_file, caption="Uploaded Chart Image", use_column_width=True)

            # Save the uploaded image locally
            image_path = f"temp_image.jpg"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.read())

                # Use the agent_team.print_response method for analysis
                try:
                    st.info("Analyzing the image, please wait...")
                    analysis_query = "Tell me about this image and give me the latest news about it."
                    image_response = selected_agent.run(
                        analysis_query,
                        images=[image_path],
                        stream=False
                    )

                    # Display results
                    st.markdown("### Image Analysis Result")
                    st.markdown(image_response.content)

                except Exception as e:
                    st.error(f"An error occurred while analyzing the image: {str(e)}")

            # Step 2: Search relevant information using DuckDuckGo
            pattern_description = image_response.content
            query_duckduckgo = f"Search for information related to the following chart pattern: {pattern_description}"
            search_response = selected_agent.run(query_duckduckgo, stream=False)

            # Step 3: Combine and display results
            st.markdown("### Image Analysis Result")
            # st.markdown(image_response.content)
            st.markdown("### Relevant Information from the Web")
            st.markdown(search_response.content)
        else:
            st.error("Please upload an image.")

# Additional information
st.info("Powered by phi.agent and various AI models.")
