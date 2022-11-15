import asyncio
import os
import webbrowser

import streamlit as st
from httpx_oauth.clients.google import GoogleOAuth2
from dotenv import load_dotenv


async def get_authorization_url(client, redirect_uri):
    """get_authorization_url returns the authorization URL where you should redirect the user to ask for their approval."""

    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url


async def get_access_token(client, redirect_uri, code):
    """get_access_token returns an OAuth2Token object for the service given the authorization code passed in the redirection callback."""
    token = await client.get_access_token(code, redirect_uri)
    return token


async def get_email(client, token):
    """Returns the id and the email of the authenticated user from the API provider. It assumes you have asked for the required scopes."""
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


def logged_in_user(user_id, user_email, client, token):
    """A function to test google oauth"""
    st.write(f"You're logged in as {user_email}")
    with st.form(key='my_form', clear_on_submit=True):
        submit_button = st.form_submit_button(label='logout')

    if submit_button:
        # await client.revoke_token("TOKEN")
        # doesnt work client.revoke_token(token)
        st.session_state.token = None
        webbrowser.open("http://localhost:8501/")


def get_google_oauth():
    """
    get_google_oauth provides Google OAuth 2.0 support
    """

    # loads env variables from .env file
    load_dotenv()

    client_id = os.environ['GOOGLE_CLIENT_ID']
    client_secret = os.environ['GOOGLE_CLIENT_SECRET']
    redirect_uri = os.environ['REDIRECT_URI']

    # Client object of OAuth2 class which provides OAuth, uses httpx-oauth library
    client = GoogleOAuth2(client_id, client_secret)

    authorization_url = asyncio.run(get_authorization_url(client=client, redirect_uri=redirect_uri))
    session_state = st.session_state.get("token")

    if session_state is None:
        try:
            code = st.experimental_get_query_params()['code']
        except Exception:
            message = f'''
                <h2>
                Login to continue <a style="font-family: 'Trebuchet MS', sans-serif" target="_self" href="{authorization_url}">Login</a>
                </h2>'''

            return (False, message)

        else:
            # Verify if token is correct:
            try:
                token = asyncio.run(get_access_token(client=client, redirect_uri=redirect_uri, code=code))
            except Exception:
                message = f'''
                    <h1>
                    This account is not allowed or page was refreshed.
                    Please try again: <a style="font-family: 'Trebuchet MS' target="_self" href="{authorization_url}">Login</a>
                    </h1>'''

                return False, message

            else:
                # Check if token has expired:
                if token.is_expired():
                    if token.is_expired():
                        message = f'''
                            <h1>
                            Login session has ended,
                            Please <a style="font-family: 'Trebuchet MS' target="_self" href="{authorization_url}"> login</a> again.
                            </h1>'''

                        return False, message
                else:
                    st.session_state.token = token
                    user_id, user_email = asyncio.run(get_email(client=client, token=token['access_token']))
                    st.session_state.user_id = user_id
                    st.session_state.user_email = user_email
                    # works if session doesnt get deleted with refresh
                    # webbrowser.open("http://localhost:8501/", new=0)
                    return True, "Success"
    else:
        return True, "Success"
