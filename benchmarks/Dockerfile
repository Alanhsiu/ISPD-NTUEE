FROM nvcr.io/nvidian/pytorch-dgl.ai:21.11
ARG DEBIAN_FRONTEND=noninteractive
RUN sed -i -e 's|disco|focal|g' /etc/apt/sources.list
RUN apt-get upgrade
RUN apt-get update
RUN echo "deb [ arch=amd64 ] https://downloads.skewed.de/apt focal main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 612DEFB798507F25
RUN apt-get upgrade -y
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 612DEFB798507F25
RUN apt-get update
RUN apt-get -y install python3-graph-tool
RUN cp -r /usr/lib/python3/dist-packages/graph_tool /usr/local/lib/python3.8/dist-packages/

RUN pip3 install --upgrade pandas

RUN pip install pyod 

RUN pip install suod

RUN pip install xgboost

RUN pip install tensorflow

RUN pip install torchmetrics

RUN pip install seaborn

RUN pip install tqdm

RUN pip install jsonlines

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu113

RUN pip install dgl-cu113 dglgo -f https://data.dgl.ai/wheels/repo.html

RUN ln -s /usr/lib/python3/dist-packages/graph_tool /opt/conda/lib/python3.8/site-packages/graph_tool

RUN apt install -y libboost-all-dev

RUN apt install -y aptitude

RUN aptitude search boost

