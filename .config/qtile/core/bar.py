import os
import re
import subprocess
import colors  
#from custom_widgets import fetch_brightness
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

colors = colors.pink

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=1,
    background=colors[0],
    foreground=colors[1],

)
extension_defaults = widget_defaults.copy()



def update_brightness():
    # Update the text of the widget with the current brightness level
    brightness_text = f"󰃠   {get_brightness()}"
    return brightness_text
def decrease_brightness():
    subprocess.run(["ddcutil", "setvcp", "10", "-", "10"])

def increase_brightness():
    subprocess.run(["ddcutil", "setvcp", "10", "+", "10"])
# Create a genpolltext widget to display the brightness level
brightness_widget = widget.GenPollText(func=update_brightness, update_interval=1)

# Add mouse callbacks to the brightness widget
brightness_widget.mouse_callbacks = {
    # Left click
    "Button1": increase_brightness,
    "Button3": decrease_brightness
}





screens = [
    Screen(
        top=bar.Bar(
            [
                                widget.Spacer(length = 7),
                widget.TextBox(
                    text ='' ,
                    fontsize = 17,
                    padding = 5,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('sh -c ~/.config/rofi/abhi/launcher.sh')},
                ),
                widget.GroupBox(
                    active = colors[1],
                    highlight_method = "line",
                    highlight_color = colors[0],
                    this_current_screen_border = colors[1]
                ),
                widget.Clipboard(max_chars=40),
                widget.Prompt(),
                widget.Mpris2(
                    format = '󰎇  {xesam:title} - {xesam:album} - {xesam:artist}',
                    max_chars = 80,
                    scroll = True,
                ),
                widget.Spacer(length = bar.STRETCH),
                widget.TextBox(
                    text =' ',
                    fontsize = 7,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('sh -c ~/.local/bin/scrshot.sh')},
                ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p "),
                widget.TextBox(
                    text ='',
                    fontsize = 7,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('sh -c ~/.local/bin/scrshot.sh')},
                ),
                widget.Spacer(length = bar.STRETCH),
                widget.Net(
                    format='  WiFi :  {down:.0f}{down_suffix}'
                ),

                #  brightness_widget,
                 widget.TextBox(
                    text ='󰕾',
                    fontsize = 15,
                ),

                                       widget.PulseVolume(
                    fmt = 'Vol: {}',
                              mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(terminal + ' -e pulsemixer')},
                ),            
                           widget.Pomodoro(
                    color_active = colors[2],
                    color_inactive = colors[1],
                    prefix_inactive = '   PoMo',
                ),
                widget.GenPollText(
                    update_interval = 300,
                    func = lambda: subprocess.check_output("printf $(whoami)", 
                    shell = True, 
                    text=True,
                                 ),
                    foreground = colors[1],
                    fmt = '❤  {}',
                              mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('emacsclient -c')},
                ),
                widget.CheckUpdates(
            distro = 'Arch',
            display_format = '󰮯   pac: {updates}',
            colour_no_updates = colors[1],
            colour_have_updates = colors[1],
        ),
                widget.TextBox(
                    text ='󰍛',
                    fontsize = 15,
                ),
                widget.Memory(format='Mem: {MemUsed: .0f}{mm}',
                              mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                              ),
                widget.TextBox(
                    text ='',
                    fontsize = 16,
mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('sh -c ~/.local/bin/scrshot.sh')},

                ),

                widget.Spacer(length = 6),
                widget.QuickExit(
                    default_text ='󰐥', 
                    countdown_format='{}',
                    fontsize = 17
                ),

               widget.Systray(
                        background=colors[0],
                        icon_size=20,
                        padding = 4
                        ),
                widget.Spacer(length = 7),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]


