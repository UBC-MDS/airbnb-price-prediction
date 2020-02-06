# Docker file for airbnb_price_prediction
# Monique Wong, Polina Romanchenko, Trevor Kwan, January 2020

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda
    
# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"
    
# install docopt python package
RUN conda install -y -c anaconda docopt requests

# install python pandas, numpy, scipy
RUN apt-get install -y python-numpy python-scipy python3-pandas

# following commands install altair stack
RUN apt-get update && apt install -y chromium && apt-get install -y libnss3 && apt-get install unzip

RUN wget -q "https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip && chown root:root /usr/bin/chromedriver && chmod +x /usr/bin/chromedriver
    
RUN conda install -y -c conda-forge altair && conda install -y vega_datasets && conda install -y selenium

# install sklearn
RUN pip install -U scikit-learn

# install R packages: knitr, docopt, testthat, checkmate
RUN Rscript -e "install.packages('knitr')"
RUN Rscript -e "install.packages('docopt')"
RUN Rscript -e "install.packages('testthat')"
RUN Rscript -e "install.packages('checkmate')"

CMD ["/bin/bash"]
