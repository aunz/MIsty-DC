FROM node:11-alpine

RUN apk add --update  python3-dev build-base openblas-dev libexecinfo-dev


#RUN pip3 install pandas==0.24.*
#RUN pip3 install numpy== 
#RUN pip3 install scipy==
#RUN pip3 install scikit-learn==0.20.*
RUN pip3 install xgboost==0.82
#RUN pip3 install flask==1.0.*

#RUN mkdir -p /app/python
#RUN mkdir -p /app/node


#COPY node/package.json /app/node
#WORKDIR /app/node
#RUN npm install


#COPY python/. /app/python
#COPY node/index.js /app/node

#WORKDIR /app

#EXPOSE 3000

#COPY entry-point.sh /app

#CMD ["./entry-point.sh"]