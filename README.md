# muzooka-artist-importer
Use the Muzzoka API to get the artist info.


## Virtual Environment

1. Install pipenv `brew install pipenv`

2. Activate the virtual environment `pipenv shell`

4. Install the dependencies `pip install fuzzywuzzy`

5. Deactivate virtual environment once done `deactivate`

## Getting artists info with Muzzoka API

1. Create an account at https://www.muzooka.com/ and create a token

2. Add the token in the env variables to be used in the python script `export MUZZOKA_TOKEN="YOUR_PRIVATE_TOKEN"`

3. Test `python importer_by_name.py static/artist_test.xml`
