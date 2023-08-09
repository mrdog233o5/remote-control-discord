#colors
RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m # No Color
MAGENTA=\033[0;35m
YELLOW=\033[0;33m

#PROGRAM NAME
PROG = SchoolCheatTools
SRC = $(wildcard *.py)
DIR = $(shell pwd)
FILES = build *.spec
#COMPILER variable

CC = pyinstaller
CFLAGS = --noconsole --uac-admin -F

#rules and recipes
clean: compile
compile: ${PROG}
${PROG}:
	@rm -rf $(PROG) $(PROG).app
	@printf "$(YELLOW)In porcess ... to compile the $(GREEN)$(PROG)${NC}\n"
	$(CC) $(CFLAGS) $(SRC)
	@printf "$(YELLOW)$(PROG)$(GREEN) compiled successfully${NC}\n"

run: compile
	@./$(PROG)

clean:
	@printf "$(YELLOW)Cleaning ...$(NC)\n"
	@rm -rf $(FILES)
	@if [ $$? -eq 0 ]; then printf "$(MAGENTA)Files $(FILES) are removed successfully\n"; else printf "$(RED)Error: Files $(FILES) are not removed\n"; fi


.PHONY: run compile clean

