# import libraries
import LangWiki.App as st
from main import search_wikipedia,summarize_text,generate_response_with_langchain, executor

def streamlit_app():
    # Set the title of the Streamlit app
    st.title("Interactive Conversation: Search, Summarization, and Chat")

    # Initialize session state for storing the current topic summary and chat history if not already present
    if 'current_topic_summary' not in st.session_state:
        st.session_state.current_topic_summary = ""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Text input for a new topic, shown only if there is no current topic summary
    if st.session_state.current_topic_summary == "":
        new_topic = st.text_input("Enter a new research topic:", key="new_topic")

        # Button to trigger search and summarization for the new topic
        if st.button("Search and Summarize"):
            with st.spinner("Searching..."):
                # Call function to search Wikipedia
                content = search_wikipedia(executor, new_topic)
                # Call function to summarize the content
                summary = summarize_text(content)
                # Store the summary in session state and append it to the chat history
                st.session_state.current_topic_summary = summary
                st.session_state.chat_history.append(f"Summary for '{new_topic}': {summary}")

    # Section to ask questions about the current topic, shown if there is a current topic summary
    if st.session_state.current_topic_summary:
        question = st.text_input("Ask a question about the current topic:", key="question")

        # Button to submit the question and get a response
        if st.button("Submit Question"):
            # Generate a response using LangChain
            response = generate_response_with_langchain(question, st.session_state.current_topic_summary)
            # Append the question and response to the chat history
            st.session_state.chat_history.append(f"Question: {question}")
            st.session_state.chat_history.append(f"Response: {response}")

        # Display the chat history
        st.subheader("Chat:")
        for message in st.session_state.chat_history:
            st.text(message)

        # Button to start researching a new topic, resets the current topic summary and chat history
        if st.button("Search New Topic"):
            st.session_state.current_topic_summary = ""
            st.session_state.chat_history = []
            

# Execute the Streamlit app
if __name__ == "__main__":
    streamlit_app()