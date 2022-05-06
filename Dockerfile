FROM apache/airflow:2.3.0

COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
# USER root
# RUN apt-get update \
#   && apt-get install -y --no-install-recommends \
#          build-essential  \
#   && apt-get autoremove -yqq --purge \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*
# USER airflow

# RUN pip install --user --upgrade pip
# RUN pip install --no-cache-dir --user -r /requirements.txt
# RUN python -m pip install matplotlib
# RUN python -m pip install pandas