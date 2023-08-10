#colors
RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m # No Color
MAGENTA=\033[0;35m
YELLOW=\033[0;33m

#PROGRAM NAME
PROG = setup SchoolCheatTools
SRC = $(wildcard *.py)
SPEC = .spec
DIR = $(shell pwd)
FILES = build *.spec
#COMPILER variable

CC = pyinstaller
CFLAGS = --clean --noconfirm# --noconsole & --uac-admin in .spec

#rules and recipes
cleanspec: compile
	@printf "$(YELLOW)Cleaning ...$(NC)\n"
	@rm -rf $(FILES)
	@if [ $$? -eq 0 ]; then printf "$(MAGENTA)Files $(FILES) are removed successfully\n"; else printf "$(RED)Error: Files $(FILES) are not removed\n"; fi

compile:
	@rm -rf $(PROG) $(PROG).app
	@printf "$(YELLOW)In porcess ... to compile the $(GREEN)$(PROG)${NC}\n"
	$(CC) $(CFLAGS) $(SPEC)
	@printf "$(YELLOW)$(PROG)$(GREEN) compiled successfully${NC}\n"

run: compile
	@./$(PROG)
