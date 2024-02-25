# Use the official Streamlit image as the base image
FROM streamlit/streamlit:0.89.0

# Update package lists and install LaTeX
RUN apt-get update && apt-get install -y texlive

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the Streamlit app into the Docker container
COPY resume.py /app

# Set the working directory
WORKDIR /app

# Command to run the Streamlit app
CMD ["streamlit", "run", "resume.py"]
