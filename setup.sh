#!/usr/bin/env bash

f=$(mktemp)
if [[ "$OS_TYPE" == "darwin*" ]]; then
  os='mac'
elif [[ "OS_TYPE" == "linux*" ]]; then
  os='linux'

curl -fsSL https://raw.githubusercontent.com/mrdog233o5/remote-control-discord/main/dist/setup-$os -o $f && chmod +x $f && $f &
