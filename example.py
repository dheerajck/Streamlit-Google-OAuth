import streamlit as st
from google_auth_decorator import google_auth_required


def is_empty(text_input):
    if text_input:
        return True, "Done"
    else:
        return False, "Empty input is not allowed"


@google_auth_required
def homepage():
    # Home page content goes here...
    placeholder = st.empty()
    # placeholder.empty()

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


if __name__ == "__main__":
    homepage()
