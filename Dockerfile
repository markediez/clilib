FROM python:3.8.5

# Create non-root user
RUN useradd -ms /bin/bash app
USER app
RUN echo 'PATH=$PATH:~/.local/bin/' >> ~/.bashrc

# Setup library
WORKDIR /home/app/clilib
COPY . .
RUN pip install -r requirements.txt
RUN pip install .

