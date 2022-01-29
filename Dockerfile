FROM python:3.9

WORKDIR /techtogetheratlanta

# Copy file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt 

# Copy required files
COPY . .

# Run Application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 