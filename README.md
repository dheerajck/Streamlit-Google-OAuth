# **Streamlit app with Google Oauth**
##### This is a simple streamlit app that uses google oauth for user authentication

## Follow the steps to properly run the web app
### I - Create a Google Cloud Platform project
Create a Google Cloud project by following instructions in the [Document here](https://developers.google.com/workspace/guides/create-project)
Delete the credentials.json and token.json in the main folder and replace them by your credentials.json and token.json if you have already generated a token
  
### II - Instructions for Google OAuth
1 - Go to the Credentials page in GCP Console
2 - Click on Create Credentials > OAuth client ID
3 - Select Web Application for Application type and fill in the name for your client
4 - Fill in Redirect URIs for your application. These are the links you want the users to be redirected back to after logging in. For example, in local environment, you can use `http://localhost:8501/`
5 - Note down the Client ID, Client Secret, Redirect URI for later  
  
6 - Enable Google - People API 
  
7 - Add Client ID, Client Secret and Redirect URI in the .env file following the sample provided
```
GOOGLE_CLIENT_ID="GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET="GOOGLE_CLIENT_SECRET"
REDIRECT_URI="http://localhost:8501/"
```  

### III - Create a virtual environment and install the requirements  
Run `pip install -U -r requirements.txt` to install the requirements  

### IV - Run the streamlit web app 
Run the streamlit Resume reviewer web app using command `streamlit run streamlit_app.py` after installing requirements specified in requirements.txt  

