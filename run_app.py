import os
import sys

# Add the src directory to the path so Python can find your modules
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
sys.path.append(src_path)

# Run Streamlit app
if __name__ == "__main__":
    import subprocess
    subprocess.run(["streamlit", "run", "src/project_s/app.py"])
