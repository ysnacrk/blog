import json 

with open('main/flask_conf.json') as config_file:
	config = json.load(config_file)


class Config:
	SECRET_KEY = config.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
	RECAPTCHA_PRIVATE_KEY = config.get('RECAPTCHA_PRIVATE_KEY')
	RECAPTCHA_PUBLIC_KEY = config.get('RECAPTCHA_PUBLIC_KEY')
