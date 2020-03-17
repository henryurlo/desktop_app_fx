
url = 'https://api.exchangerate-api.com/v4/latest/USD'
response = requests.get(url)
data = response.json()
# The data variable will look like the dictionary below
{
"base": "USD",
	"date": "2020-14-20",
	"time_last_updated": 1553092232,
	"rates": {
		"USD": 1,
		"AUD": 1.4882,
		"CAD": 1.325097,
		"...": 1.311357,
		"...": 7.4731, etc. etc.
	}
}
