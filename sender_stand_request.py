import requests
import configuration
import data


#   Creating a user
def post_new_user(user_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
	                     json = user_body,
	                     headers = data.headers)


#   Creating a kit
def post_new_client_kit(kit_body, auth_token):  
    headers_copy = data.headers.copy()  
    headers_copy["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,  
        	json=kit_body,  
        	headers=headers_copy)
