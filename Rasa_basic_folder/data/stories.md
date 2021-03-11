
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - slot{"location": "Chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* budget{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_ask_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - action_check_location
    - slot{"location": "Warangal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Warangal"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "dfdjnnvfinvjg.rfdfd@thok.gov.in"}
    - slot{"email": "dfdjnnvfinvjg.rfdfd@thok.gov.in"}
    - action_check_email
    - slot{"email": "dfdjnnvfinvjg.rfdfd@thok.gov.in"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* affirm{"email": "cdcchaudhari@gmail.co.in"}
    - slot{"email": "cdcchaudhari@gmail.co.in"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.co.in"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_4
* restaurant_search
    - utter_ask_location
* location{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "cchaudha@usc.edu"}
    - slot{"email": "cchaudha@usc.edu"}
    - action_check_email
    - slot{"email": "cchaudha@usc.edu"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Bijapur"}
    - slot{"location": "Bijapur"}
    - action_check_location
    - slot{"location": "Bijapur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* budget{"budget": "max budget 300"}
    - slot{"budget": "max budget 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Bijapur"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Jamshedpur"}
    - slot{"location": "Jamshedpur"}
    - action_check_location
    - slot{"location": "Jamshedpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Jamshedpur"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location": "Hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* goodbye
    - utter_goodbye
    - action_restart





## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"location": "Jamshedpur"}
    - slot{"location": "Jamshedpur"}
    - action_check_location
    - slot{"location": "Jamshedpur"}
    - utter_ask_cuisine
* deny
    - utter_goodbye
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Bokaro Steel City"}
    - slot{"location": "Bokaro Steel City"}
    - action_check_location
    - slot{"location": "Bokaro"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Bokaro"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - action_check_location
    - slot{"location": "Delhi NCR"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North indian"}
    - slot{"cuisine": "North indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North indian"}
    - utter_ask_budget
* budget{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_ask_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_email
* send_email{"email": "asasdfdfd@ghghgh.com"}
    - slot{"email": "asasdfdfd@ghghgh.com"}
    - action_check_email
    - slot{"email": "asasdfdfd@ghghgh.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_invalid_location_twice_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "malvan"}
    - slot{"location": "malvan"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location{"location": "malvan"}
    - slot{"location": "malvan"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_goodbye
    - action_restart

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"location": "Cuttack"}
    - slot{"location": "Cuttack"}
    - action_check_location
    - slot{"location": "Cuttack"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_ask_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "Cuttack"}
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* budget{"location": "Amravati"}
    - slot{"location": "Amravati"}
    - action_check_location
    - slot{"location": "Amravati"}
    - utter_ask_budget
* budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Amravati"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_14
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* budget{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - action_check_location
    - slot{"location": "Warangal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_budget
* budget{"budget": "less 300"}
    - slot{"budget": "less 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Warangal"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart


## interactive_story_15
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* budget{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_ask_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - utter_send_email
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - utter_email_sent
    - reset_slots
    - action_restart


## interactive_story_restaurant_search_no_email_16
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "Chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_1_17
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_allentities_no_email_18
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Mumbai", "budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart


## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"budget": "Lesser than Rs. 300", "cuisine": "American", "location": "Chandigarh"}
    - slot{"budget": "Lesser than Rs. 300"}
    - slot{"cuisine": "American"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - slot{"location": "Chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - action_check_location
    - slot{"location": "Chandigarh"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_send_email
* send_email{"email": "cdcchaudhari@gkall.co.ink"}
    - slot{"email": "cdcchaudhari@gkall.co.ink"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gkall.co.ink"}
    - action_send_email
    - reset_slots
    - utter_email_sent


## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"budget": "expensive"}
    - slot{"budget": "expensive"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* location{"location": "jhansi"}
    - slot{"location": "jhansi"}
    - action_check_location
    - slot{"location": "Jhansi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "Jhansi"}
    - utter_send_email
* send_email
    - utter_ask_emailid
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* goodbye{"bye": "thank you"}
    - utter_goodbye
    - action_restart


## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"budget": "affordable", "cuisine": "thai", "location": "Amritsar"}
    - slot{"budget": "affordable"}
    - slot{"cuisine": "thai"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location": "Amritsar"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_search_restaurants
    - slot{"location": "Amritsar"}
* goodbye
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"budget": "affordable", "location": "Chennai"}
    - slot{"budget": "affordable"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location": "Chennai"}
    - action_ask_budget
    - slot{"budget": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mediterranean"}
    - slot{"cuisine": "mediterranean"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_send_email
* deny{"deny": "Nope"}
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart



## interactive_story_23
* greet
    - utter_greet
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* location{"location": "greenworld"}
    - slot{"location": "greenworld"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location{"location": "antartica"}
    - slot{"location": "antartica"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_24
* greet{"greet": "Hello"}
    - utter_greet
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* location{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart



## interactive_story_25
* greet{"greet": "Hello"}
    - utter_greet
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* location{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - utter_email_sent
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_wrong_cuisine_twice_26
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi NCR"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "maharashtrian"}
    - slot{"cuisine": "maharashtrian"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_wrong_budget_twice_27
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* budget{"budget": "-100"}
    - slot{"budget": "-100"}
    - action_ask_budget
    - slot{"budget": null}
    - utter_ask_budget
* budget{"budget": "budget sudget"}
    - slot{"budget": "budget sudget"}
    - action_ask_budget
    - slot{"budget": null}
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_wrong_email_once_28
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "giv@@99@@gmail"}
    - slot{"email": "giv@@99@@gmail"}
    - action_check_email
    - slot{"email": null}
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart


## interactive_story_wrong_correct_cuisine_wrong_correct_email_29
* greet
    - utter_greet
* restaurant_search{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - action_check_location
    - slot{"location": "Dehradun"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "malaysian"}
    - slot{"cuisine": "malaysian"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Dehradun"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "fgfhfghgfbcvfgtg.ghgfh.fgdfg.li"}
    - slot{"email": "fgfhfghgfbcvfgtg.ghgfh.fgdfg.li"}
    - action_check_email
    - slot{"email": null}
    - utter_send_email
* send_email{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - slot{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - action_check_email
    - slot{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_wrong_correct_budget_wrong_correct_email_30
* greet
    - utter_greet
* restaurant_search{"location": "Belgaum"}
    - slot{"location": "Belgaum"}
    - action_check_location
    - slot{"location": "Belgaum"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* budget{"budget": "cheaper"}
    - slot{"budget": "cheaper"}
    - action_ask_budget
    - slot{"budget": null}
    - utter_ask_budget
* budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Belgaum"}
    - utter_send_email
* send_email{"email": "cddfgfgdfgdfg.gfhgf.h.gdhg"}
    - slot{"email": "cddfgfgdfgdfg.gfhgf.h.gdhg"}
    - action_check_email
    - slot{"email": null}
    - utter_send_email
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* goodbye{"bye": "thnx"}
    - utter_goodbye
    - action_restart

## interactive_story_wrong_wrong_email_twice_31
* greet
    - utter_greet
* restaurant_search{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - action_check_location
    - slot{"location": "Coimbatore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* budget{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_ask_budget
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "Coimbatore"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "champ123.gfdfgdf.fdgdfg.dfgfdg"}
    - slot{"email": "champ123.gfdfgdf.fdgdfg.dfgfdg"}
    - action_check_email
    - slot{"email": null}
    - utter_send_email
* send_email{"email": "fdgvdfvdfgfd.dgdfgd.fdgfgdfg.gfdgfd"}
    - slot{"email": "fdgvdfvdfgfd.dgdfgd.fdgfgdfg.gfdgfd"}
    - action_check_email
    - slot{"email": null}
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart


## interactive_story_goodbye_start_32
    - utter_greet
* goodbye
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart


## interactive_story_33
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_34
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* deny
    - utter_goodbye
    - action_restart

## interactive_story_35
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_check_location
    - slot{"location": "Delhi NCR"}
    - utter_ask_cuisine
* deny{"deny": "no"}
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_36
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye{"location": "Kakinada"}
    - slot{"location": "Kakinada"}
    - action_check_location
    - slot{"location": "Kakinada"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* goodbye
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_37
* deny
    - utter_goodbye
    - action_restart


## interactive_story_no_search_start_38
* deny
    - utter_goodbye
    - action_restart

## interactive_story_39
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_40
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "Delhi NCR"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_41
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_direct_email_ask_42
* greet
    - utter_greet
* send_email{"cuisine": "american", "location": "Mumbai", "budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_emailid
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_direct_email_ask_wrong_wrong_email_43
* greet
    - utter_greet
* send_email{"cuisine": "american", "location": "Mumbai", "budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_emailid
* send_email{"email": "fgfhfghgfbcvfgtg.ghgfh.fgdfg.li"}
    - slot{"email": "fgfhfghgfbcvfgtg.ghgfh.fgdfg.li"}
    - action_check_email
    - slot{"email": null}
    - utter_ask_emailid
* send_email{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - slot{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - action_check_email
    - slot{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_direct_email_ask_wrong_correct_email_44
* greet
    - utter_greet
* send_email{"cuisine": "american", "location": "Mumbai", "budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_emailid
* send_email{"email": "aaabbbcccddd.gfhgf.h.gdhg"}
    - slot{"email": "aaabbbcccddd.gfhgf.h.gdhg"}
    - action_check_email
    - slot{"email": null}
    - utter_send_email
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* goodbye{"bye": "thnx"}
    - utter_goodbye
    - action_restart 

## interactive_story_45
* greet
    - utter_greet
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - utter_ask_location
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_46
* greet
    - utter_greet
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - utter_ask_location
* goodbye{"deny": "No"}
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_47
* greet{"greet": "hello"}
    - utter_greet
* budget{"budget": "Less than Rs. 300"}
    - slot{"budget": "Less than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - utter_ask_location
* location{"location": "Jaldandhar"}
    - slot{"location": "Jaldandhar"}
    - action_check_location
    - slot{"location": "Jalandhar"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_48
* greet
    - utter_greet
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - action_ask_budget
    - slot{"budget": "low"}
    - utter_ask_location
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"location": "Surat"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "Surat"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_49
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* deny
    - utter_goodbye
    - reset_slots
    - action_restart

## interactive_story_50
* greet{"greet": "Hello"}
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* location{"location": "Puducheryy"}
    - slot{"location": "Puducheryy"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location{"location": "pondicheryy"}
    - slot{"location": "pondicheryy"}
    - action_check_location
    - slot{"location": "Chennai"}
    - utter_ask_budget
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart

## interactive_story_51
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* location{"location": "amdabaad"}
    - slot{"location": "amdabaad"}
    - action_check_location
    - slot{"location": "Ahmedabad"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart


## interactive_story_cuisine_first_ideal_path_52
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi NCR"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart


## interactive_story_cuisine_first_wrong_email_twice_53
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi NCR"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "fgfhfghgfbcvfgtg.ghgfh.fgdfg.li"}
    - slot{"email": "fgfhfghgfbcvfgtg.ghgfh.fgdfg.li"}
    - action_check_email
    - slot{"email": null}
    - utter_send_email
* send_email{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - slot{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - action_check_email
    - slot{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart



## interactive_story_cuisine_first_wrong_email_once_54
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi NCR"}
    - utter_ask_budget
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "cddfgfgdfgdfg.gfhgf.h.gdhg"}
    - slot{"email": "cddfgfgdfgdfg.gfhgf.h.gdhg"}
    - action_check_email
    - slot{"email": null}
    - utter_send_email
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* goodbye{"bye": "thnx"}
    - utter_goodbye
    - action_restart



    

## interactive_story_budget_first_ideal_path_55
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_budget_first_wrong_email_twice_56
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "fgfhfghgfbcvfgtg.ghgfh.fgdfg.li"}
    - slot{"email": "fgfhfghgfbcvfgtg.ghgfh.fgdfg.li"}
    - action_check_email
    - slot{"email": null}
    - utter_send_email
* send_email{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - slot{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - action_check_email
    - slot{"email": "fgfhffgfgfgfdg@ghgfh.fgdfg.li"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart


## interactive_story_budget_first_wrong_email_once_57
* greet{"greet": "hello"}
    - utter_greet
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "cdcchaudhari@gmail.com"}
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_check_email
    - slot{"email": "cdcchaudhari@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
* goodbye{"bye": "thnx"}
    - utter_goodbye
    - action_restart
  

## interactive_story_wrong_cuisine_once_and_email_58
* greet{"greet": "hey"}
    - utter_greet
* restaurant_search{"budget": "Lesser than Rs. 300", "location": "Mumbai"}
    - slot{"budget": "Lesser than Rs. 300"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - action_ask_budget
    - slot{"budget": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "himalayan"}
    - slot{"cuisine": "himalayan"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* affirm
    - utter_ask_emailid
* send_email{"email": "divesh.gaonkar@gmail.com"}
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_check_email
    - slot{"email": "divesh.gaonkar@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart


## interactive_story_59
* greet{"greet": "Hello"}
    - utter_greet
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* location{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart


## interactive_story_60
* greet{"greet": "Hello"}
    - utter_greet
* budget{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_ask_budget
    - slot{"budget": "high"}
    - utter_ask_location
* location{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_send_email
* deny
    - utter_goodbye
    - action_reset_slot
    - reset_slots
    - action_restart      