# Use a python base image
FROM python:3.10-slim-buster

# Install Python and pip
RUN apt update && apt install -y python3 python3-pip

# Set the working directory
WORKDIR /docker_learn

# Copy requirements.txt
COPY ./model.joblib ./

COPY ./predict20924.py ./
COPY requirements.txt ./

# Install dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

# Copy the rest of the application code


# Expose the port (if applicable)
# EXPOSE 8000

# Command to run the application
# CMD ["python", "predict19924.py"]
EXPOSE 8501

# Run the app
# CMD ["streamlit", "run", "app.py"]
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "predict20924.py", "--server.port=8501", "--server.address=0.0.0.0"]

# ENTRYPOINT ["streamlit", "run","predict20924.py", "--server.port=8501", "--server.address=0.0.0.0"]
