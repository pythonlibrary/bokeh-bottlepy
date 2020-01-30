# bokeh-bottlepy

Deploy your data visualization with bokeh on internet. 

# project description

This project is the example code for the article https://pythonlibrary.net/2020/01/29/deploy-data-disualisation-with-bokeh/

The baseline of the web site powered by [bottle](https://bottlepy.org/docs/dev/index.html)] is from this great work: [bottle-bootstrap](https://github.com/arsho/bottle-bootstrap).

The data visualization is implemented with [bokeh](https://docs.bokeh.org/en/latest/index.html), as bokeh provides very great embed functionalities, It can generate javascript and div code with a simple python method call. With the SimpleTemplate Engine that the bottle provides, we can plug the code snippets in the HTML template very easily

The pre-processed dataset is also included in this repo

# how to run

* install the python packages, basically pandas, bokeh and bottle are all we need, you can also choose to use `pip -r requirements.txt`
* run the server `python app.py`
* open link http://localhost:8080/

# demo

* demo service is also available on Heroku: https://china-aqi-data-visulazition.herokuapp.com/