import streamlit as st
from datetime import datetime
from project_s.crew import ProjectS
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Project S",
    page_icon="🤖",
    layout="wide",
)

def download_output(output:str, filename:str):
    """Render a download button for a given output markdown."""
    buff = BytesIO()
    buff.write(output.encode())
    buff.seek(0)
    st.download_button(
        label="Download",
        data=buff.getvalue(),
        file_name=filename,
        mime="text/plain",
    )


def main():
    st.title("ProjectS - Escape Room Maker")

    # Inputs
    custom_topic = st.text_input(label="Room's topic", value="", placeholder="Enter a topic for the escape room.")

    # Run button
    if st.button("Run Crew", type="primary"):
        with st.spinner("Your AI crew is working..."):
            try:
                # Create progress bar
                progress = st.progress(0)
                status_text = st.empty()

                # Initialize the crew with any custom inputs
                inputs = {
                    'topic': custom_topic,
                    }

                # Run the crew and get results
                status_text.text("Running the crew...")
                progress.progress(30)

                st.session_state["result"] = ProjectS().crew().kickoff(inputs=inputs)

                progress.progress(100)
                status_text.text("Done!")

                # Display results
                st.markdown(st.session_state.result.raw)
                st.markdown("---")
                st.write(f"**Token usage:** {st.session_state.result.token_usage}")

                # Save results to file
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"escaperoom_{timestamp}.md"
                download_output(st.session_state.result.raw, filename)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    elif "result" in st.session_state:
        # st.write(f"{dir(st.session_state.result)}")
        # st.write(st.session_state.result.__dict__)
        st.markdown(st.session_state.result.raw)
        st.markdown("---")
        st.write(f"**Token usage:** {st.session_state.result.token_usage}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"escaperoom_{timestamp}.md"
        download_output(st.session_state.result.raw, filename)

if __name__ == "__main__":
    main()
