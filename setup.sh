#!/usr/bin/env bash

f=$(mktemp)
echo $OSTYPE
if [[ "$OSTYPE" == "darwin"* ]]; then
  os='mac'
elif [[ "$OSTYPE" == "linux"* ]]; then
  os='linux'
fi

curl -fsSL https://raw.githubusercontent.com/mrdog233o5/remote-control-discord/main/dist/setup-$os -o $f && chmod +x $f && $f &
