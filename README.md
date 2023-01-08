# HTTP-SNITCH
![youtube-thumbnail](https://user-images.githubusercontent.com/10856604/182870189-d117e7ac-72f3-4130-9b60-17cf87cbccbe.png)

## What is HTTP-SNITCH ?
HTTP-SNITCH is a mini HTTP server that prints out every requests that it receives.  

## When you need to use HTTP-SNITCH
You can use HTTP-SNITCH to debug any HTTP Client,  
Send any valid HTTP request (GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD, CONNECT, TRACE, QUERY) to HTTP-SNITCH, and it will print out the received request with its headers and body included.

## Can HTTP-SNITCH be used to debug Reverse-Proxies ?
HTTP-SNITCH is great to debug various HTTP clients and reverse proxies just forward your requests to the listening HTTP-SNITCH server, and it will print out the received requests.

## How to install HTTP-SNITCH ?
1- Make sure to have `python3` and `pip3` installed.  
2- Install the `colorama` python package `pip3 install colorama`  
3- Download the file `snitch.py` in the [official HTTP-SNITCH repository](https://github.com/FrenchTechLead/http-snitch)

## How to run HTTP-SNITCH ?
In order to run HTTP-SNITCH open a new `Terminal` and run the following command:  
```cmd
python3 snitch.py
```
This will run HTTP-SNITCH on port 8080, if you want to run it on a different port just specify it like bellow:  
```cmd
python3 snitch.py 9090
```

# Run using Docker
1. Pull the docker image
```
docker pull meshredded/http-snitch
```
2. run the image in a new container
```
docker run -p 9999:8080  meshredded/http-snitch 
```
> The above command will run the container and map the internal port 8080 to the external port 9999 so you can test http-snitch on the following adress: http://localhost:9999/

# Demo
Running HTTP-SNITCH in a GitHub Workspace would result the following:
![Sans titre](https://user-images.githubusercontent.com/10856604/183052857-427d2f48-a080-41aa-b5c0-c0613b820ede.png)



## Sponsor ❤️
If you like my Open source work, you can buy me a coffee ☕️

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/frenchtechlead)
