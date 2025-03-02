import streamlit as st
from datetime import datetime
from project_s.crew import ProjectS

# Set page config
st.set_page_config(
    page_title="Project S",
    page_icon="🤖",
    layout="wide",
)

def main():
    st.title("ProjectS - Escape Room Maker")   

    # Inputs
    custom_topic = st.text_input("Room's topic", "Boiling water")
    
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
                
                result = ProjectS().crew().kickoff(inputs=inputs)
                
                progress.progress(100)
                status_text.text("Done!")
                
                # Display results
                st.header("Results")
                st.markdown(result)
                
                # Save results to file
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"escaperoom_{timestamp}.md"
                
                with open(filename, "w") as f:
                    f.write(result)
                
                st.success(f"Results saved to {filename}")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
