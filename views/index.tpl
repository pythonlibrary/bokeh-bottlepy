<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Deploy Bokeh Data Visualization with Bottlepy">
	<meta name="author" content="datamate">
	<link rel="icon" href="/static/favicon.ico">		
	<title>China AQI</title>
	<link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
	<script type="text/javascript" src="/static/jquery.min.js"></script>
	<script type="text/javascript" src="/static/bootstrap.min.js"></script>	
	<script src="https://cdn.bokeh.org/bokeh/release/bokeh-1.4.0.min.js"></script>
	<script src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-1.4.0.min.js"></script>
	<script src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-1.4.0.min.js"></script>
</head>
<body>
	<!-- Static navbar -->
	<nav class="navbar navbar-default navbar-static-top">
		<div class="container">
			<div class="row">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a class="navbar-brand" href="#">China AQI Data Visualization</a>
				</div>
				<div id="navbar" class="navbar-collapse collapse">
					<ul class="nav navbar-nav navbar-right">
						<li><a href="../">Home</a></li>
						<li><a href="https://github.com/pythonlibrary/bokeh-bottlepy">On Github</a></li>
					</ul>
				</div><!--/.nav-collapse -->
			</div>
		</div>
	</nav>
	<div class="container">
		<div class="row">
			<div class="jumbotron">
			<h2>中国AQI数据可视化</h2>
				<p>这是一个基于bottlepy, bokeh和Bootstrap的一个数据可视化部署的示例项目，采用了中国从2017年到2019年的AQI信息数据作为项目的演示数据。</p>
			</div>
		</div>
		<div class="row">
			{{!data["plot1_div"]}}
		</div>
		</br></br></br></br>
		<div class="row">
			{{!data["plot2_div"]}}
		</div>
		</br></br></br></br>
		<div class="row">
			{{!data["plot3_div"]}}
		</div>
		<!--./row-->
		<div class="row">
			<hr>
			<footer>
				<p>&copy; 2020 {{data["developer_organization"]}}.</p>
			</footer>			
		</div>
	</div> 
	<!-- /container -->
</body>
{{!data["plot_script"]}}
</html>