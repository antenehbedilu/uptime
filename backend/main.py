from fastapi import FastAPI

#customize metadata configurations and define URLs for API documentation
app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi', redoc_url=None, title='Uptime', description='**Uptime** a *RESTful API* to get instant notifications, manage monitors and check your uptime statistics on the go.', summary='Easy-to-use, self-hosted monitoring tool.', version='0.0.1', contact={'name': 'Uptime', 'url': 'https://github.com/antenehbedilu/uptime', 'email': 'hello@antenehbedilu.com'}, license_info={'name': 'MIT License', 'url': 'https://raw.githubusercontent.com/antenehbedilu/uptime/main/LICENSE'})
