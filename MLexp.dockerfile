# Use a python base image
FROM python:3.10-slim-buster

# Install Python and pip
RUN apt update && apt install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY ./model.joblib ./

COPY ./test_m.py ./
COPY ./requirements.txt ./

RUN pip install -r requirements.txt



# Command to run the application
# CMD ["python", "test_m.py"]
EXPOSE 8501


HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "test_m.py", "--server.port=8501", "--server.address=0.0.0.0"]

