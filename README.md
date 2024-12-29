## Python selenium script to automate test scenario for invalid login credentails..

First you need to have installed dependencies and before that  create a virtual environment

#### Steps to create virtual environment:
for ubuntu machine:

command in terminal

```sh
python3 -m venv venv
```
Activate it

```sh
source venv/bin/activate
```
#### Get repostitory 


```sh
git clone https://github.com/strikertushar19/selenium-web-testing.git
```
#### Install dependencies


```sh
pip install -r requirements.txt
```



Now you need to replace the path of geckdriver which is web driver used
to create a test firefox web browser instance so install it and specify the web driver path
in code inside main.py

Here is the link to officila documentation where it is desribed how to download
 link: https://pypi.org/project/selenium/

 After setting up the driver
 Run the project:
 
 #### commnad to run project

```sh
python3 main.py

```

On an averga time taken to run 1 test on the website url depends on speed of connection 
in my case website is bit slow in giving response so it was taking significant amount around 120 seconds on 
an average for 1 test case to run successfully.