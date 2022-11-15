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
        # doesnt work client.revoke_token(token)
        st.session_state.token = None
        webbrowser.open("http://localhost:8501/")


def is_empty(text_input):
    if text_input:
        return True, "Done"
    else:
        return False, "Empty input is not allowed"


def homepage():
    """
    homepage loads the home page(streamlit support for custom url was not found so root is considered as home)
    if user is authenticated successfully else loads a google signin option
    """

    status, google_auth_response = get_google_oauth()


    placeholder = st.empty()
    # placeholder.empty()

    if status:
        with placeholder.container(), st.form(key='home', clear_on_submit=True):
            st.title("Home page")
            text_input = st.text_input(label='Input something')
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            status, message = is_empty(text_input)
            if status:
                st.write(message)
            else:
                st.warning(message)

        logout()

    else:
        st.write(google_auth_response, unsafe_allow_html=True)


def main():
    # Streamlit: each refresh/action loads entire webpage again
    homepage()


if __name__ == "__main__":
    main()
