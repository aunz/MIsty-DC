FROM continuumio/miniconda3

RUN pip install numpy==1.16.* 
RUN pip install scipy==1.2.*
RUN pip install pandas==0.24.*
RUN pip install scikit-learn==0.20.*
RUN pip install xgboost==0.82
RUN pip install flask==1.0.*

RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs

RUN mkdir -p /app/python
RUN mkdir -p /app/node


COPY node/package.json /app/node
WORKDIR /app/node
RUN npm install


COPY python/. /app/python
COPY node/index.js /app/node

WORKDIR /app

EXPOSE 3000

COPY entry-point.sh /app

CMD ["./entry-point.sh"]