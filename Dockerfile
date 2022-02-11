FROM ubuntu:latest

RUN   apt-get update; \ 
      apt-get install -y python3; \
      apt-get install -y python3-pip
      

RUN   mkdir game; \
      pip3 install git; \
      pip3 install pgzrun; \
      git clone https://github.com/Vgobi/pong.git; \
      python3 pong.py


      

