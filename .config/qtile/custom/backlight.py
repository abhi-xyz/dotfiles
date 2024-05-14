import shlex
from functools import partial

from libqtile.command.base import expose_command
from libqtile.log_utils import logger
from libqtile.widget import base


class Backlight(base.InLoopPollText):
    """A simple widget to show the current brightness of a monitor using ddcutil.

    You can also bind keyboard shortcuts to the backlight widget with:

    .. code-block:: python

        from libqtile.widget import backlight
        Key(
            [],
            "XF86MonBrightnessUp",
            lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.UP)
        )
        Key(
            [],
            "XF86MonBrightnessDown",
            lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.DOWN)
        )
    """

    defaults = [
        ("update_interval", 0.2, "The delay in seconds between updates"),
        ("step", 10, "Percent of backlight every scroll changed"),
        ("format", "{percent:2.0%}", "Display format"),
        ("change_command", "ddcutil setvcp 10 {0}", "Command to change brightness using ddcutil"),
        ("min_brightness", 0, "Minimum brightness percentage"),
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(Backlight.defaults)
        self._future = None

    def finalize(self):
        if self._future and not self._future.done():
            self._future.cancel()
        base.InLoopPollText.finalize(self)

    def _get_brightness(self):
        try:
            output = subprocess.check_output(["ddcutil", "getvcp", "10"])
            return int(output.decode("utf-8").strip())
        except subprocess.CalledProcessError as e:
            logger.debug("Failed to get brightness: %s", e)
            raise RuntimeError("Failed to get brightness")

    def _change_brightness(self, value):
        try:
            subprocess.check_call(shlex.split(self.change_command.format(value)))
        except subprocess.CalledProcessError as e:
            logger.warning("Failed to change brightness: %s", e)

    def poll(self):
        try:
            brightness = self._get_brightness()
        except RuntimeError as e:
            return "Error: {}".format(e)

        percent = brightness / 100.0
        return self.format.format(percent=percent)

    @expose_command()
    def change_backlight(self, direction, step=None):
        if not step:
            step = self.step
        if self._future and not self._future.done():
            return
        new = now = self._get_brightness()
        if direction == ChangeDirection.DOWN:
            new = max(now - step, self.min_brightness)
        elif direction == ChangeDirection.UP:
            new = min(now + step, 100)
        if new != now:
            self._future = self.qtile.run_in_executor(self._change_brightness, new)

