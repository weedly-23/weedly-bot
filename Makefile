-include .env
export 
start:
	@python -m weedly_bot.bot
lint:
	@mypy weedly_bot
	@flake8 weedly_bot
