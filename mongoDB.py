import json
import requests
import sys

if __name__ == "__main__":
	args = sys.argv[1:]
	api_key = args[0]

	url = "https://data.mongodb-api.com/app/data-djqwt/endpoint/data/beta/action/findOne"

	payload = json.dumps({
		"collection": "listingsAndReviews",
		"database": "sample_airbnb",
		"dataSource": "DansCluster",
		"projection": {}
	})

	headers = {
		'Content-Type': 'application/json',
		'Access-Control-Request-Headers': '*',
		'api-key': f'{api_key}'
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
