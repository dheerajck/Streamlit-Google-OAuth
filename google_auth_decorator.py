import functools

import streamlit as st

from google_oauth_support import get_google_oauth
import webbrowser


def logout():
    """
    logout loads the submit button for logout
    """

    with st.form(key='logout', clear_on_submit=True):
        submit_button = st.form_submit_button(label='logout')

    if submit_button:
        # await client.revoke_token("TOKEN")
        # client.revoke_token(token) isnt deleting token from session
        st.session_state.token = None
        st.session_state.token = None
        webbrowser.open("http://localhost:8501/")


def google_auth_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # google oauth
        status, google_auth_response = get_google_oauth()

        if status:
            # Run the decorated function
            result = func(*args, **kwargs)
            logout()
            return result
        else:
            # Display the Google sign-in button
            st.write(google_auth_response, unsafe_allow_html=True)

    return wrapper
