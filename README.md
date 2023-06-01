# hexagoon-Mongodb
microarchitecture in python connected to mongodb

## 1 CLONE THE PROJECT

-> GIT Clone https://github.com/fabriciogl/hexagoon-Mongodb.git

## 2 POETRY

--> Having python 3.10 installed, use ``` pip install poetry ```

## 4 INSTALL PACKAGES

--> Inside the root app folder run ``` poetry install ```

## 4 SECRETS

--> create a ```.secrets.toml``` file with the following content inside the root folder, replacing the password for each enviroment:

--> replace the values with your own settings  
--> ``` [default] ``` is mandatory, even if you don't use as an environment.    
--> ``` [production] [development] [testing] ``` are used when necessary  

<code>
[default]<br/>  
root_user = "root" <br/>  
root_role = "root" <br/>
root_pass = "cookies" <br/>
root_email = "root@hexagoon.space" <br/> 
jwt_hash = "longHash" <br/>  
jwt_algo = "HS256" <br/>  
db_name = "hexagoon" <br/>  
db_address = "" <br/>  
[production] <br/>  
root_user = "root" <br/>  
root_role = "root" <br/>
root_pass = "cookies" <br/>
root_email = "root@hexagoon.space" <br/> 
jwt_hash = "longHash" <br/>  
jwt_algo = "HS256" <br/>  
db_name = "hexagoon" <br/>  
db_address = "" <br/>   
[development] <br/>  
root_user = "root" <br/>  
root_role = "root" <br/>
root_pass = "cookies" <br/>
root_email = "root@hexagoon.space" <br/> 
jwt_hash = "longHash" <br/>  
jwt_algo = "HS256" <br/>  
db_name = "hexagoon" <br/>  
db_address = "" <br/>   
[testing] <br/>  
root_user = "root" <br/>  
root_role = "root" <br/>
root_pass = "cookies" <br/>
root_email = "root@hexagoon.space" <br/> 
jwt_hash = "longHash" <br/>  
jwt_algo = "HS256" <br/>  
db_name = "hexagoon" <br/>  
db_address = "" <br/>   
</code>


## 5 

--> install postgres with docker

``` docker pull mongodb:latest```

## 6

--> configure postgres

``` docker run --name mongo -p 27017:27017 -d mongo:tag```

## 7

--> Using Pycharm, create a server run/debug configuration and add following variables to env

    - ENV_FOR_DYNACONF=development;

## 8

--> run aplication on Pycharm

## 9 

--> stopping your app

stop pycharm run/debug server and ``` docker stop mongodb ```

--> restarting your app

``` docker start mongodb ``` and start pycharm run/debug server
