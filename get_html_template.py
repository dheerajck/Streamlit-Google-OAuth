LOGIN_TO_CONTINUE_HTML = (
    lambda authorization_url: f'''
        <h1 style="font-family: sans-serif; font-size: 20px; font-weight: bold;">
            Login to continue
            <a style="font-family: 'Trebuchet MS'; font-size: 20px; color: #0077C9;" target="_self"
                href="{authorization_url}">Login</a>
        </h1>
        '''
)


ACCOUNT_NOT_ALLOWED_HTML = (
    lambda authorization_url: f'''
        <h1 style="font-family: sans-serif; font-size: 20px; font-weight: bold;">
            This account is not allowed or the page was refreshed.<br>
            Please try again:
            <a style="font-family: 'Trebuchet MS'; font-size: 20px; color: #0077C9;" target="_self"
                href="{authorization_url}">Login</a>
        </h1>
        '''
)


USER_SESSION_ENDED_HTML = (
    lambda authorization_url: f'''
        <h1 style="font-family: sans-serif; font-size: 20px; font-weight: bold;">
            Login session has ended,
            Please login again to continue:
            <a style="font-family: 'Trebuchet MS'; font-size: 20px; color: #0077C9;" target="_self" 
            href="{authorization_url}">Login</a>
        </h1>
        '''
)
