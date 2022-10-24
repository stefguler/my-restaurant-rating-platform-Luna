# Pull miniconda from docker hub as base image
FROM continuumio/miniconda3

# Create folder
RUN mkdir -p /backend

#pass all the files and folders from local folder to image
COPY ./backend /backend

# create the environment inside the docker container
RUN /opt/conda/bin/conda env create -f /backend/requirements.yml

WORKDIR /backend

# we set the path were all the python pacakages are
ENV PATH /opt/conda/envs/luna_project/bin:$PATH

#activate app
RUN echo "source activate luna_project" >~/.bashrc
