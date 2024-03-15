#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

# Utilities
run nm-applet &
blueman-applet &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/bin/dunst &
run volumeicon &



