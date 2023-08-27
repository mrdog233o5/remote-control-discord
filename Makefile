#colors
RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m # No Color
MAGENTA=\033[0;35m
YELLOW=\033[0;33m

#PROGRAM NAME
PROG1 = setup.py
PROG2 = main.py
SRC = $(wildcard *.py)
SPEC = .spec
DIR = $(shell pwd)
FILES = build *.spec

#COMPILER variable
CC = pyinstaller
CFLAGS = --clean --noconfirm --noconsole --uac-admin -F


#rules and recipes
all: buildmac zipmacapp cleanspec

cleanspec:
	@printf "$(YELLOW)Cleaning spec...$(NC)\n"
	@rm -rf $(FILES)
	@if [ $$? -eq 0 ]; then printf "$(MAGENTA)Files $(FILES) are removed successfully\n"; else printf "$(RED)Error: Files $(FILES) are not removed\n"; fi

buildmac:
	@rm -f dist/$(PROG1) dist/$(PROG1).app dist/$(PROG1) dist/$(PROG2).app
	@printf "$(YELLOW)In porcess ... to compile the $(GREEN)$(PROG1)${NC}\n"
	$(CC) $(CFLAGS) $(PROG1)
	@printf "$(YELLOW)In porcess ... to compile the $(GREEN)$(PROG2)${NC}\n"
	$(CC) $(CFLAGS) $(PROG2)
	@printf "$(YELLOW)$(PROG1) $(PROG2)$(GREEN) compiled successfully${NC}\n"
	@mv dist/setup dist/setup-mac
	@mv dist/main dist/main-mac

buildlinux:
	@rm -f dist/$(PROG1) dist/$(PROG1).app dist/$(PROG1) dist/$(PROG2).app
	@printf "$(YELLOW)In porcess ... to compile the $(GREEN)$(PROG1)${NC}\n"
	$(CC) $(CFLAGS) $(PROG1)
	@printf "$(YELLOW)In porcess ... to compile the $(GREEN)$(PROG2)${NC}\n"
	$(CC) $(CFLAGS) $(PROG2)
	@printf "$(YELLOW)$(PROG1) $(PROG2)$(GREEN) compiled successfully${NC}\n"
	@mv dist/setup dist/setup-linux
	@mv dist/main dist/main-linux

run: build*
	@open ./dist/*

zipmacapp: buildmac
	@zip -r dist/setup.app.zip dist/setup.app
	@zip -r dist/main.app.zip dist/main.app
	@if [ $$? -eq 0 ]; then printf "$(MAGENTA)Files dist(*.app) are zipped successfully\n"; else printf "$(RED)Error: Files dist(*.app) are not zipped\n"; fi

clean: cleanspec
	@printf "$(YELLOW)Cleaning...$(NC)\n"
	@rm -rf dist
	@if [ $$? -eq 0 ]; then printf "$(MAGENTA)Files dist(*) are removed successfully\n"; else printf "$(RED)Error: Files dist(*) are not removed\n"; fi
