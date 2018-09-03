# Using lightweight alpine image
FROM python

# Defining working directory
WORKDIR /app

# Install dependencies.
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Add application code
ADD . /app

# Start app
EXPOSE 5000
ENTRYPOINT ["/app/bootstrap.sh"]