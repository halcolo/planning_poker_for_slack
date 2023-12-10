FROM ubuntu:24.04


# Configure apt
ENV ENVIRONMENT=DEV
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y python3 python3-fann2 \
    && apt-get -y install --no-install-recommends apt-utils 2>&1

# Install git, process tools, lsb-release (common in install instructions for CLIs)
RUN apt-get -y install git procps lsb-release

# Install pylint
# RUN pip install pylint

# Install any missing dependencies for enhanced language service
RUN apt-get install -y libicu[0-9][0-9]

WORKDIR /app

# # Install Python dependencies from requirements.txt if it exists
# COPY . .
# RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt && rm requirements.txt*; fi

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ssh-add ~/.ssh/id_rsa

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash