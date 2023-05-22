# AppSailPythonDemo

This code will work when you are using catalyst serve command and may not work when deployed.
Reason: In the tutorial we were using python virtual environment to create the application, but the same may not work when deployed to resolve this issue, deactivate your virtual environment using `deactivate ` command and install the packages with -t falg.

Example:
`pip install flask -t .`

Typically, Python frameworks are unable to manage all incoming requests in a production environment. To effectively handle these requests, it is necessary to employ tools such as gunicorn. If you are utilizing gunicorn, please consult the documentation at
https://docs.gunicorn.org/en/stable/ 
for configuring it in your application. Additionally, remember to modify the command in app-config.json to accommodate the changes.

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
