FROM python:3.11.1-bullseye

ENV VIRTUAL_ENV=/opt/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create virtual env
RUN apt-get update \
    && apt-get install -y \
    && python3 -m venv $VIRTUAL_ENV \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose port
EXPOSE 80

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

# Run the application
COPY . ./
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit.py"]
