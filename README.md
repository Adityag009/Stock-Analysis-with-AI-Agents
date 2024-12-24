# Stock-Analysis-with-AI-Agents

# Stock Analysis with AI Agents

This project demonstrates how to leverage multiple AI agents for stock market analysis and chart pattern identification using a Streamlit interface. Users can switch between different AI models, including OpenAI’s GPT, Gemini, and Groq’s Llama, through Grok API integration. The application provides functionalities for comparing stock data and analyzing chart patterns, making it an innovative solution for investment research and financial insights.

---

## Project Overview

### Features
1. **AI Agents for Stock Analysis**:
   - Analyze stock prices, fundamentals, and analyst recommendations.
   - Compare multiple stocks based on user input.
2. **Chart Pattern Analysis**:
   - Upload chart images for AI-driven pattern identification.
   - Retrieve relevant insights using web search tools.
3. **Dynamic Model Switching**:
   - Users can select their preferred AI agent (OpenAIChat, Gemini, or Groq) from the interface.
4. **Streamlit-Powered UI**:
   - Intuitive user interface for seamless interaction.

### AI Models and Tools
- **OpenAIChat (GPT-4o)**: Handles natural language queries and provides detailed stock analysis.
- **Gemini (Gemini-2.0-flash-exp)**: Optimized for fast and accurate investment insights.
- **Groq (Llama-3.3-70b-versatile)**: A versatile AI model focused on comprehensive data analysis.
- **YFinanceTools**: Fetches live stock prices, fundamentals, and analyst recommendations.
- **DuckDuckGo**: Conducts web searches for additional insights.

---

## File Structure

### Main Files
- **`Streamlit.py`**: The primary interface script for running the Streamlit application.
- **`Ai-agent.py`**: Script defining the base configuration for AI agents.
- **`gemini-agent.py`**: Script for configuring and running the Gemini AI agent.
- **`openai-agent.py`**: Script for configuring and running the OpenAI AI agent.
- **`demo.py`**: A demo script for testing agent functionalities.
- **`requirements.txt`**: Lists all the dependencies required to run the project.

### Configuration Files
- **`.env`**: Environment variables for secure API key management.

### Supporting Files
- **`temp_image.jpg`**: Temporary storage for uploaded chart images.
- **`README.md`**: Documentation file (this document).

---

## How to Run

### Prerequisites
1. **Python Environment**:
   - Ensure Python 3.9+ is installed.
2. **Dependencies**:
   - Install required libraries using:
     ```bash
     pip install -r requirements.txt
     ```
3. **Environment Variables**:
   - Create a `.env` file with your API keys (OpenAI, Groq, and others as needed).

### Running the Application
1. Navigate to the project directory.
2. Run the Streamlit application:
   ```bash
   streamlit run Streamlit.py
   ```
3. Open the application in your web browser at `http://localhost:8501`.

---

## Usage

### Switching AI Models
1. Select the desired AI model (OpenAIChat, Gemini, or Groq) from the dropdown menu.
2. The selected agent will handle subsequent queries.

### Stock Analysis
1. Choose the "Compare Stocks" option.
2. Enter stock symbols (e.g., `AAPL, TSLA`) in the input box.
3. Click the "Analyze" button to view stock prices, fundamentals, and analyst recommendations.

### Chart Pattern Analysis
1. Choose the "Analyze Chart Pattern" option.
2. Upload a chart image in PNG, JPG, or JPEG format.
3. The AI will analyze the image and display identified patterns.
4. Relevant insights will be retrieved using DuckDuckGo.

---

## Example Scenarios
1. **Stock Comparison**:
   - Input: `AAPL, TSLA`
   - Output: Comparison of stock prices, PE ratios, market caps, and more.

2. **Chart Pattern Analysis**:
   - Upload: A head-and-shoulders chart.
   - Output: Pattern identification with supporting information from the web.

---

## Dependencies

The following Python libraries are required:
- `streamlit`
- `phi`
- `dotenv`
- `markdown`

---

## Future Improvements
1. Add more AI models for greater variety.
2. Enhance chart pattern recognition using vision AI models.
3. Incorporate real-time data streaming for stock updates.

---

## License
This project is open-source and licensed under the MIT License.

---

## Acknowledgments
- **Phi Framework**: For providing the AI agent integration.
- **Streamlit**: For the interactive UI framework.
- **YFinanceTools**: For live stock data.
- **DuckDuckGo**: For search capabilities.

---

For more details, explore the source code or reach out to the contributors.

