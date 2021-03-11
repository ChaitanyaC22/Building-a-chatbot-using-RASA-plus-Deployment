from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
from rasa_sdk.events import AllSlotsReset
import zomatopy
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import pandas as pd
import numpy as np


tier_1_2_cities = ['Agra', 'Ahmedabad', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum',\
				 'Bengaluru', 'Bhavnagar', 'Durg Bhilai', 'Mumbai', 'Bhopal', 'Bhubaneswar', 'Bijapur', 'Bikaner', 'Bilaspur',\
				  'Bokaro', 'Chandigarh', 'Chennai', 'Coimbatore', 'Cuttack', 'Dehradun', 'Delhi NCR', 'Dhanbad', 'Dindigul', \
				  'Durgapur', 'Erode', 'Delhi NCR', 'Firozabad', 'Delhi NCR', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Delhi NCR', \
				  'Guwahati', 'Gwalior', 'Hamirpur', 'Dharwad', 'Hyderabad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', \
				  'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Karnal', 'Kochi', 'Kolhapur', 'Kolkata',\
				   'Kollam', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mangalore', 'Mathura', 'Meerut', \
				   'Moradabad', 'Mumbai', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Delhi NCR', 'Patna', 'Chennai',\
				    'Allahabad', 'Pune', 'Purulia', 'Raipur', 'Rajahmundry', 'Rajkot', 'Ranchi', 'Rourkela', 'Salem', 'Sangli',\
				     'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 'Chennai', 'Trivandrum', 'Thrissur','Vadodara','Varanasi',\
				     'Ujjain','Virar','Tirunelveli','Vellore','Vijayawada','Visakhapatnam','Warangal']

##List of Tier 1 and Tier 2 cities
tier_1_2_city_names= [city.lower() for city in tier_1_2_cities]

##Validating Location
def Check_Location(loc, city_names= tier_1_2_city_names):  
	config={"user_key":"337f3a03601af0bbcc30b2e3506be18d"}
	zomato = zomatopy.initialize_app(config)
	location_detail=zomato.get_location(loc, 1)
	location_json = json.loads(location_detail)
	number_of_loc = len(location_json['location_suggestions'])

	try:
		if number_of_loc==0:
			return {'location_result': 'Not Found!', 'location_name': None}
		elif (location_json['location_suggestions'][0]['city_name']).lower() not in tier_1_2_city_names:
			return {'location_result': "Sorry! We do not operate in this area yet.", 'location_name': None}
		else:
			return {'location_result': "Location Found!", 'location_name': location_json['location_suggestions'][0]['city_name']}
	except:
		dispatcher.utter_message("Sorry, please enter a valid request!")


class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):

		loc = tracker.get_slot('location')
		check= Check_Location(loc)

		return[SlotSet('location',check['location_name'])]



class Actionvalidatecuisine(Action):
	def name(self):
		return 'action_validate_cuisine'

	def run(self,dispatcher,tracker,domain):

		cuisine_list = ['chinese','mexican','italian','american','south indian','north indian']
		requested_cuisine = tracker.get_slot('cuisine')

		if requested_cuisine is not None:
			if requested_cuisine.lower() in cuisine_list:
				return[SlotSet('cuisine', requested_cuisine)]
			else:
				dispatcher.utter_message("Sorry, the requested cuisine is invalid. Please provide a valid cuisine.")
				return[SlotSet('cuisine', None)]
		else:
			dispatcher.utter_message("Sorry, I could not understand the requested cuisine. Please re-enter the cuisine.")
			return [SlotSet('cuisine', None)]



class ActionAskBudget(Action):
	def name(self):
		return 'action_ask_budget'

	def run(self,dispatcher,tracker,domain):
		high_list= ['more than 700', 'more than rs. 700', 'more than rs 700', 'more 700', '>700', '> 700', 'high', 'elite', 'expensive', 'luxurious', '700+', '700 plus', 'greater than 700', 'higher than 700', 'more than 700', 'greater 700', 'costly']
		low_list=['lesser than rs. 300', 'lesser than rs.300', 'lesser than rs300', 'lesser than rs. 300','less 300', 'lesser than rs 300', 'affordable', 'less than rs 300', 'lesser than 300', 'less than 300', '<300', '< 300', 'max 300', 'below 300', 'until 300', 'low range', 'low', 'limit 300', 'max lim 300', 'max limit 300', 'max budget 300', 'less than rs. 300']
		mid_list= ['between 300 and 700','between rs.300 to 700', 'between rs300 to 700', 'rs. 300 to 700', '300-700', 'between 300-700', 'between rs. 300 to 700', 'between rs 300 to 700', 'between 300 to 700', '300 to 700', 'mid range', 'mid', 'moderate price range', 'moderate range', 'moderate']
		requested_budget = tracker.get_slot('budget')
		requested_budget_lower = (requested_budget.lower()).strip()
		try:
			if requested_budget_lower in low_list:
				return ([SlotSet('budget', 'low')])
			elif requested_budget_lower  in high_list:
				return ([SlotSet('budget', 'high')])
			elif requested_budget_lower  in mid_list:
				return ([SlotSet('budget', 'mid')])
			else:
				dispatcher.utter_message("Sorry, the budget entry is invalid. Please re-enter a valid request!")
				return ([SlotSet('budget', None)])

		except:
			dispatcher.utter_message("Sorry, the entry is invalid. Please re-enter a valid request!")
			return ([SlotSet('budget', None)])
			


class ActionSearchRestaurants(Action):

	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		config = {"user_key": "337f3a03601af0bbcc30b2e3506be18d"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail = zomato.get_location(loc, 1)
		budget_detail = tracker.get_slot('budget')

		if budget_detail == 'low':
			min_val = 0
			max_val = 300
		elif budget_detail == 'mid':
			min_val = 301
			max_val = 700
		else:
			min_val = 701
			max_val = 10000000
		
		d1 = json.loads(location_detail)
		lat = d1["location_suggestions"][0]["latitude"]
		lon = d1["location_suggestions"][0]["longitude"]
		cuisines_dict = {'american': 1, 'mexican': 73, 'chinese': 25, 'italian': 55, 'north indian': 50, 'south indian': 85}
		results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
		d = json.loads(results)
		results_shown = int(d['results_shown'])
		name = []
		location = []
		avg_cost = []
		agg_rating = []
		response = ""
		for i in range(0, results_shown):
			name.append(d['restaurants'][i]['restaurant']['name'])
			location.append(d['restaurants'][i]['restaurant']['location']['address'])
			avg_cost.append(int(d['restaurants'][i]['restaurant']['average_cost_for_two']))
			agg_rating.append(float(d['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']))
		df_display = pd.DataFrame({'Name': name, 'Location': location, 'average_cost_for_two': avg_cost, 'Ratings': agg_rating})
		df_display = df_display[(df_display['average_cost_for_two'] >= min_val) & (df_display['average_cost_for_two'] <= max_val)].sort_values('Ratings', ascending=False)
		df_display = df_display.head(5)
		if len(df_display)!=0:
			for index , rec in df_display.iterrows():
				response = response + rec['Name'] + " in " + rec['Location'] + " " + "has been rated " + \
	            str(rec['Ratings']) + "\n"
			dispatcher.utter_message("" + response)
			return [SlotSet('location', loc)]
		else:
			dispatcher.utter_message("No records found!")



class ActionValidateEmail(Action):

	def name(self):
		return 'action_check_email'

	def run(self, dispatcher, tracker, domain):
		user_email = tracker.get_slot('email')
		regex = '^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
		if user_email is not None:
			if (re.search(regex, user_email)):
				return [SlotSet('email', user_email)]
			else:
				dispatcher.utter_message("Sorry, the provided email is invalid, please recheck the email id provided ")
				return [SlotSet('email', None)]
		else:
			dispatcher.utter_message("Sorry, I could'nt understand the input provided. Please provide a valid email id again.")
			return [SlotSet('email', None)]


class ActionSendEmail(Action):

	def name(self):
		return 'action_send_email'

	def run(self,dispatcher, tracker, domain):
		try: 
			config = {"user_key": "337f3a03601af0bbcc30b2e3506be18d"}
			zomato = zomatopy.initialize_app(config)
			loc = tracker.get_slot('location')
			cuisine = tracker.get_slot('cuisine')
			location_detail = zomato.get_location(loc, 1)
			budget_detail = tracker.get_slot('budget')
			if budget_detail == 'low':
				min_val = 0
				max_val = 300
			elif budget_detail == 'mid':
				min_val = 301
				max_val = 700
			else:
				min_val = 701
				max_val = 1000000
			d1 = json.loads(location_detail)
			lat = d1["location_suggestions"][0]["latitude"]
			lon = d1["location_suggestions"][0]["longitude"]
			cuisines_dict = {'american': 1, 'mexican': 73, 'chinese': 25, 'italian': 55, 'north indian': 50,'south indian': 85}
			results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
			d = json.loads(results)
			results_shown = int(d['results_shown'])
			name = []
			location = []
			avg_cost = []
			agg_rating = []
			for i in range(0, results_shown):
				name.append(d['restaurants'][i]['restaurant']['name'])
				location.append(d['restaurants'][i]['restaurant']['location']['address'])
				avg_cost.append(int(d['restaurants'][i]['restaurant']['average_cost_for_two']))
				agg_rating.append(float(d['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']))

			df = pd.DataFrame({'Restaurant Name': name, 'Restaurant locality address': location, 'Average budget for two people': avg_cost, 'Zomato user rating': agg_rating})
			df = df[(df['Average budget for two people'] >= min_val) & (df['Average budget for two people'] <= max_val)].sort_values('Zomato user rating', ascending=False)
			df = df.head(10)
			if len(df)!=0:
				html = """\
				<html>
				  <head>Below are the requested Restaurant details
				  </head>
				  <body>
				    {0}
				  </body>
				</html>
				""".format(df.to_html(index=False))
				sender_address = 'restaurant.upgradchatbot@gmail.com'
				sender_pass = 'upgrad#123'
				user_email = tracker.get_slot('email')
				receiver_address = user_email

				message = MIMEMultipart('alternative')
				message['From'] = sender_address
				message['To'] = receiver_address
				message['Subject'] = "Hey Foodie!! Details of Restaurants in " + tracker.get_slot('location') + ' as per your custom preferences'

				message.attach(MIMEText(html, 'html'))

				# Create SMTP session for sending the mail
				session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
				session.starttls()  # enable security

				session.login(sender_address, sender_pass)  # login with mail_id and password
				text = message.as_string()
				session.sendmail(sender_address, receiver_address, text)
				session.quit()
				return[AllSlotsReset()]
			else:
				dispatcher.utter_message("No records found! Email not sent.")
		except:
			dispatcher.utter_message("Sorry, the entry is Invalid. Please re-enter a valid request!")

class ActionResetSlot(Action):
	def name(self):
		return 'action_reset_slot'

	def run(self,dispatcher, tracker, domain):
		return[AllSlotsReset()]


class ActionRestart(Action):
	def name(self):
		return 'action_restart'

	def run(self,dispatcher, tracker, domain):
		return[Restarted()]


