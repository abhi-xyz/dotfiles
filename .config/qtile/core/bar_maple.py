import os
import re
import subprocess
import colors
from custom.fetch_brightness import get_brightness
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

colors = colors.pink

widget_defaults = dict(
    font="Maple Mono",
    fontsize=12,
    padding=5,
    background=colors[0],
    foreground=colors[1],
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                                widget.Spacer(length = 7),
                widget.TextBox(
                    text ='' ,
                    fontsize = 17,
                    padding = 2,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('sh -c ~/.config/qtile/rofi/launchers/launcher.sh')},
                ),
                                                widget.GroupBox(
                    active = colors[1],

                                    #   hide_unused = "true",
                    highlight_method = "line",
                    highlight_color = colors[0],
                    this_current_screen_border = colors[1]
                ),

                widget.Clipboard(
                    max_chars= 100,
                    scroll = 'true',
                    foreground = colors[2]),
                widget.Prompt(),
                widget.Mpris2(
                    format = '󰎇  {xesam:title} - {xesam:album} - {xesam:artist}',
                    max_chars = 80,
                    scroll = True,
                ),
                widget.Spacer(length = bar.STRETCH),

                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                widget.Spacer(length = bar.STRETCH),
                widget.Spacer(length = 0),
                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                widget.Net(
                    format='WiFi : {down:.0f}{down_suffix}',
                    margin_x =8,
                    margin_y = 20,
                    padding_x = 20,
                    padding_y = 20,
                ),
                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                widget.Memory(
                    update_interval = 0.1,
                format='Mem :{MemUsed: .0f}{mm}'),
                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                widget.PulseVolume(
                    fmt = 'Vol : {}'
                    ),
                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                widget.GenPollText(
                        func=update_brightness,
                        mouse_callbacks = {
                            'Button5': lambda: qtile.cmd_spawn('sh -c ~/.bin/qtile_brightness_down'),
                            'Button4': lambda: qtile.cmd_spawn('sh -c ~/.bin/qtile_brightness_up'),
                                           },
                                   update_interval=0.2),
                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                 widget.GenPollText(
                    update_interval = 300,
                    func = lambda: subprocess.check_output("printf $(whoami)", shell = True, text=True,),
                    foreground = colors[1],
                    fmt = '❤ {}',
                              mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('emacsclient -c')},
                ),
                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                widget.QuickExit(
                    default_text ='󰐥', 
                    countdown_format='{}',
                    fontsize = 17
                ),

                widget.TextBox(text ='|' , fontsize = 17, padding = 5, ),
                widget.WidgetBox(
                    close_button_location = "right",
                    text_open = '󰁑',
                    text_closed = '󰁑',
                    fontsize = 21,
                    widgets=[
                        widget.Systray(),

                        ]
                    ),
                widget.Spacer(length = 7),
            ],
            30,
            opacity=1,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # x11_drag_polling_rate = 60, # if drag is laggy
    ),
]


