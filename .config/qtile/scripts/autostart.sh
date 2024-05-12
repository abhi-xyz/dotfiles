#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}


#feh --bg-fill ~/.config/qtile/wallpapers/rainworld.png &
#wallpaper for other Arch based systems
#feh --bg-fill /usr/share/archlinux-tweak-tool/data/wallpaper/wallpaper.png &
#start the conky to learn the shortcuts
#(conky -c $HOME/.conky/conkymy) &
#(conky -c $HOME/.config/qtile/scripts/system-overview) &
#start sxhkd to replace Qtile native key-bindings
run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &


#starting utility applications at boot time
run nm-applet &
playerctld &
emacs --daemon &
clipmenud &
#run pamac-tray &
#run xfce4-power-manager &
kdeconnect-indicator &
numlockx on &
#blueberry-tray &
picom --config $HOME/.config/qtile/picom/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#/usr/lib/xfce4/notifyd/xfce4-notifyd &

#starting user applications at boot time
#run volumeicon &
nitrogen --restore &
