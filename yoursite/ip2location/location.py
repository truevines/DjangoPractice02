from geolite2 import geolite2

#location clss
class geolocation:
	def __init__(self, ip):
		result=geolite2.reader().get(ip)
		self.country=result['country']['names']['en']
		self.state=result['subdivisions'][0]['names']['en']
		self.city=result['city']['names']['en']
		
