# AppSailPythonDemo

This code will work when you are using catalyst serve command and may not work when deployed.
Reason: In the tutorial we were using python virtual environment to create the application, but the same may not work when deployed to resolve this issue, deactivate your virtual environment using `deactivate ` command and install the packages with -t falg.

Example:
`pip install flask -t .`

Python Frameworks in general won't handle all the incoming requests in production environment, we need to use tools like gunicorn to handle all the request. If you are using gunicorn refer to https://docs.gunicorn.org/en/stable/ for the set-up in your application and change the command in app-config.json to `python3 -u -m gunicorn main:app --bind 0.0.0.0:$X_ZOHO_CATALYST_LISTEN_PORT`

app-config.json after changes
```
{
	"command": "python3 -u -m gunicorn main:app --bind 0.0.0.0:$X_ZOHO_CATALYST_LISTEN_PORT",
	"buildPath": "/myLocation/AppSail/AppSailPython",
	"stack": "python_3_9",
	"env_variables": {},
	"memory": 256
}
```
