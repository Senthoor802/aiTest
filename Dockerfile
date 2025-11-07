FROM selenium/standalone-chrome

WORKDIR /usr/app


# Install some dependencies
RUN sudo apt-get update
RUN sudo apt-get install -y software-properties-common
RUN sudo add-apt-repository -y ppa:deadsnakes/ppa
RUN sudo apt-get update
RUN sudo apt-get install -y python3.9 python3.9-venv python3.9-dev unixodbc-dev build-essential
# Install Allure
RUN sudo curl -o allure-2.13.7.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.7/allure-commandline-2.13.7.tgz
RUN sudo tar -zxvf allure-2.13.7.tgz -C /opt/
RUN sudo ln -s /opt/allure-2.13.7/bin/allure /usr/bin/allure

# Install pip using ensurepip
RUN sudo python3.9 -m ensurepip --upgrade

# Upgrade pip using --ignore-installed
RUN sudo python3.9 -m pip install --upgrade pip --ignore-installed
RUN sudo python3.9 -m pip install --upgrade setuptools wheel --ignore-installed

# Install Python dependencies
COPY ./docker-requirements.txt ./
RUN sudo python3.9 -m pip install -r docker-requirements.txt


# # Install ChromeDriver manually
RUN sudo curl -o chromedriver_linux64.zip -Ls https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/135.0.7049.84/linux64/chromedriver-linux64.zip && \
    sudo apt-get install -y unzip && \
    sudo unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
    sudo mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    sudo chmod 755 /usr/local/bin/chromedriver

RUN sudo chmod 755 /usr/local/bin/chromedriver


# COPY ../../drivers/chromedriver.exe /usr/local/bin/chromedriver
# RUN sudo chmod +x /usr/local/bin/chromedriver

RUN ls -l /usr/local/bin/chromedriver
RUN /usr/local/bin/chromedriver --version


# Copy application code
COPY ./ ./
RUN sudo python3.9 -m pip install ./utilities/PyAuto-3.4.0-py3-none-any.whl
RUN sudo python3.9 -m pip install reportportal-client==5.0.12 numpy==1.23 webdriver-manager==3.4.2
RUN sudo python3.9 -m pip install --upgrade webdriver-manager
# Set the Python path
ENV PYTHONPATH=/usr/app

# Ensure correct permissions
RUN sudo chmod -R 755 /usr/app/utilities

# Ensure correct permissions for the reports directory
RUN mkdir -p /usr/app/reports && sudo chmod -R 777 /usr/app/reports

# Ensure correct permissions for the resources directory
RUN mkdir -p /usr/app/resources && sudo chmod -R 777 /usr/app/resources && sudo chown -R seluser:seluser /usr/app/resources

WORKDIR /usr/app/tests/step_defs/

# Default command
ENTRYPOINT ["sh", "-c", "PYTHONPATH=/usr/app sudo python3.9 RunTest.py --docker"]
CMD ["--tags", "bdd"]