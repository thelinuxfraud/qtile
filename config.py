##########################
# title: qtile           #
# tags: config.py        #
# author: thelinuxfraud  #
##########################


import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.backend.wayland import InputConfig
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration

# Startup Applications
@hook.subscribe.startup_once
def autostart():
    if qtile.core.name == "x11":
        autostartscript = "~/.config/qtile/scripts/x11-autostart.sh"
    elif qtile.core.name == "wayland":
        autostartscript = "~/.config/qtile/scripts/wayland-autostart.sh"

    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])

if qtile.core.name == "wayland":
    os.environ["XDG_SESSION_DESKTOP"] = "qtile:wlroots"
    os.environ["XDG_CURRENT_DESKTOP"] = "qtile:wlroots"


mod = "mod4"
terminal = "kitty" 
home = os.path.expanduser('~')

keys = [

# ESSENTIALS #

    # Important keys
    Key([mod, "shift"], "m", lazy.spawn("dmenu_run -i"), desc="Dmenu app"),
    Key([mod, "shift"], "d", lazy.spawn("wofi --show drun"), desc="App launcher"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "Space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "m", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn prompt widget"),

    # Multimedia keys 
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +3%"), desc="Raise brightness level by 3%"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 3-%"), desc="Lower brightness level by 3%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 3%+"), desc="Raise volume level by 3%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 3%-"), desc="Lower volume level by 3%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute or unmute volume level"),

    # Applications
    Key([mod, "shift"], "l", lazy.spawn("spotify"), desc="Music player"),
    Key([mod, "shift"], "Return", lazy.spawn("thunar"), desc="File manager"),
    Key([mod, "shift"], "e", lazy.spawn("emacs"), desc="Doom Emacs"),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Web browser"),
    Key([mod], "d", lazy.spawn("discord"), desc="Discord app"),
    Key([mod], "p", lazy.spawn("grim"), desc="Screenshot tool"),



# WINDOW FOCUSING #

    # Change Window Focus
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

    # Resize Windows
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # Shift focused window
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # Change workspaces
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),

            # Move focused window to workspace 1-10 / follow
            Key([mod, "shift"],i.name,lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name),),

            # Moved focused window to workspace 1-10 / stay
            Key([mod, "control"], i.name, lazy.window.togroup(i.name), desc="move focused window to group {}".format(i.name)),
        ])

def init_layout_theme():
    return {"margin":8,
            "border_width":2,
            "border_focus": "#81a1c1",
            "border_normal": "#2e3440"
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(**layout_theme, new_client_position='top'),
    layout.Max(),
    ]


widget_defaults = dict(
    font="RobotoMono Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4c566a",
                    background = "#2e3440"
                ),
                widget.CurrentLayoutIcon(
                    padding = 4,
                    scale = 0.7,
                    foreground = "#d8dee9",
                    background = "#2e3440"
                ),
                 widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4c566a",
                    background = "#2e3440"
                ),
                widget.GroupBox(
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    margin_y = 2,
                    margin_x = 3,
                    padding_y = 2,
                    padding_x = 3,
                    borderwidth = 0,
                    disable_drag = True,
                    active = "#4c566a",
                    inactive = "#2e3440",
                    rounded = False,
                    highlight_method = "text",
                    this_current_screen_border = "#d8dee9",
                    foreground = "#4c566a",
                    background = "#2e3440"
                ),
                 widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4c566a",
                    background = "#2e3440"
                ),
                widget.Prompt(
                    font = "RobotoMono Nerd Font",
                    fontsize = 12,
                    background = "#2e3440",
                    foreground = "#d8dee9"
                ),
                widget.WindowName(
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    foreground = "#d8dee9",
                    background = "#2e3440"
                    ),
                widget.Sep(
                    foreground = "#4c566a",
                    background = "#2e3440",
                    padding = 5,
                    linewidth = 1
                    ),
                widget.Net(
                    foreground = "#2e3440",
                    background = "#2e3440",
                    font = 'RobotoMono Nerd Font Bold',
                    fontsize = 12,
                    format = '{down} ↓↑ {up}',
                    interface = 'wlan0',
                    decorations = [
                        RectDecoration (
                            colour = "#8fbcbb",
                            padding_y = 3,
                            radius = 2,
                            filled = True
                            ),
                        ],
                        ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4c566a",
                    background = "#2e3440"
                    ),
                widget.CPU(
                    background = "#2e3440",
                    foreground = "#2e3440",
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    decorations = [
                        RectDecoration (
                            colour = "#ebcb8b",
                            padding_y = 3,
                            radius = 2,
                            filled = True
                        ),
                    ],),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "4c566a",
                    background = "#2e3440"
                    ),
                widget.Memory(
                    measure_mem = 'G',
                    foreground = "#2e3440",
                    background = "#2e3440",
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    decorations = [
                        RectDecoration (
                            colour = "#88c0d0",
                            padding_y = 3,
                            radius = 2,
                            filled = True
                        ),
                    ],),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4c566a",
                    background = "#2e3440"
                    ),
                widget.DF(
                    visible_on_warn = False,
                    background = "#2e3440",
                    foreground = "#2e3440",
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    decorations = [
                        RectDecoration (
                            colour = "#a3be8c",
                            padding_y = 3,
                            radius = 2,
                            filled = True
                        ),
                    ],),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    background = "#2e3440",
                    foreground = "#4c566a"
                    ),
                widget.Clock(
                    foreground = "#2e3440",
                    background = "#2e3440",
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    format = "%D %H:%M",
                    decorations = [
                        RectDecoration (
                            colour = "#81a1c1",
                            padding_y = 3,
                            radius = 2,
                            filled = True
                        ),
                    ],),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4c566a",
                    background = "#2e3440"
                    ),
                widget.UPowerWidget(
                    background = "#2e3440",
                    border_colour = '#d8dee9',
                    border_critical_colour = '#bf616a',
                    border_charge_colour = '#d8dee9',
                    fill_low = '#ebcb8b',
                    fill_charge = '#a3be8c',
                    fill_critical = '#bf616a',
                    fill_normal = '#d8dee9',
                    percentage_low = 0.4,
                    percentage_critical = 0.2,
                    font = "RobotoMono Nerd Font"
                    ),
                widget.StatusNotifier(
                        background = "#2e3440",
                        icon_size = 20,
                        padding = 5
                        ),
                #widget.Systray(
                #    background = "#2e3440",
                #    icon_size = 20,
                #    padding = 5,
                #    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4c566a",
                    background = "#2e3440" 
                    ),
                widget.OpenWeather(
                    app_key = "4cf3731a25d1d1f4e4a00207afd451a2",
                    cityid = "4997193",
                    format = '{main_temp}° {icon}',
                    metric = False,
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    background = "#2e3440",
                    foreground = "#d8dee9",
                    decorations = [
                        RectDecoration (
                            colour = "#2e3440",
                            padding_y = 3,
                            radius = 2,
                            filled = True 
                        ),
                    ],),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    background = "#2e3440",
                    foreground = "#4c566a"
                    ),
            ],
            # Sets bar height
           24,
        ),
        # Set wallpaper
        wallpaper="/home/blake/Pictures/wallpapers/nord/nord-river.png",
        wallpaper_mode='fill',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list

main = None

follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(border_width=2, border_focus="#5e81ac", border_normal="#2e3440",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = False 

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {
        "1160:4122:DELL0A20:00 0488:101A Touchpad": InputConfig(tap=True),
    }

# Something about java being dumb?
wmname = "LG3D"



