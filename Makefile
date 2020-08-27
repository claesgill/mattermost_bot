
create-bot:
	@python3 bot_generator.py

files := $(shell ls -1 generated_bots/)
list-bots:
ifeq ($(files),)
	@echo "\e[31mNo bots found in 'generated_bots/'. Try 'make create-bot'\e[0m"
else
	@for file in $(files); do echo '\e[32m'$$file'\e[0m'; done;
endif

test-bot:
	@python3 generated_bots/$(bot).py \
	&& \
	echo '\e[32mTest completed\e[0m' \
	|| \
	echo '\e[31mTest failed.\nFollow python stack-trace or' \'$(bot).py\' 'does not exist.\nUsage: make test-bot bot=<botname>\e[0m'