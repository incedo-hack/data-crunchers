FROM python:3.6-slim

RUN set -x \
	&& buildDeps=' \
		curl \
		g++ \
		gcc \
		libssl-dev \
		libxml2-dev \
		libxslt-dev \
		make \
		zlib1g-dev \
	' \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set the working directory to /apps
WORKDIR /apps

# Install the modules
ADD requirements.txt /apps
RUN pip install -r requirements.txt

# Copy the content from currect directory
ADD __init__.py settings.py database.py recommendation.py handler.py /apps/