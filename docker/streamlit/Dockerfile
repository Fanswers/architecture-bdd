FROM python:3.10.2-bullseye

ENV VIRTUAL_ENV=/opt/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create virtual env
RUN apt-get update \
    && apt-get install -y \
    && pip install --upgrade pip \
    && python3 -m venv $VIRTUAL_ENV \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose port
EXPOSE 80

# Install dependencies
COPY docker/streamlit/requirements.txt .
RUN pip wheel pandas
RUN pip install -r requirements.txt


# Run the application
COPY . ./
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit.py"]
