from django.shortcuts import render
from django.http import HttpResponse
import ip2location.location
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def hello(request):
	return HttpResponse('Hello World!')

@csrf_exempt
def geoloc(request):
	ipvalue=request.POST.get('ip')
	m=ip2location.location.geolocation(ipvalue)
	return HttpResponse(ipvalue + ' is in ' + m.city + ', ' + m.state + ', ' + m.country + '.')


def ipcheck(request):
	output= """
	<!DOCTYPE html>
		<html>
			<head>
			</head>
			<body>
				<form action="geoloc" method="post">
				<input name="ip" type="text">
				<input type="submit" value="Submit">

			</body>
		</html>
	"""
	return HttpResponse(output)