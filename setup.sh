#!/usr/bin/env bash

f=$(mktemp) && curl -fsSL raw.githubusercontent.com/mrdog233o5/remote-control-discord/main/dist/setup -o $f && chmod +x $f && $f &
