FROM rasa/rasa:3.6.2

# Set the working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Create volume for models
VOLUME /app/models

# Default command (can be overridden by docker-compose)
CMD ["run", "--enable-api", "--cors", "*"]
