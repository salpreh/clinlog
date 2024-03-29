from colorama import init, Fore, Back, Style


class Logger(object):
    """
    Class to log styled messages to stdout.

    Attributes:
        log_level(str|num): Verbosity level. Valid values (class properties 
            avaliable):
            - debug or `0` (default)
            - info or `1` 
            - warning or `2` 
            - error or `3`
    """

    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

    def __init__(self, log_level=0):
        init()
        self._error_tag = ''
        self._info_tag = ''
        self._warn_tag = ''
        self._confirm_tag = ''
        self._debug_tag = ''
        self._print_tag = ''

        self._max_verbosity = 0
        self._min_verbosity = 3
        self._log_level = self._get_log_level_id(log_level)

    def _get_log_level_id(self, log_level):
        """
        Returns a valid log level number
        """
        if type(log_level) is str:
            return self._get_log_level_dict().get(log_level, 0)

        if log_level > self._min_verbosity:
            return 3

        elif log_level < self._max_verbosity:
            return 0
        
        else:
            return log_level

    def _get_log_level_dict(self):
        return {
            'debug': 0,
            'info': 1,
            'warning': 2,
            'error': 3,
            'confirm': 3
        }

    def error(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        """
        Prints a message to stdout with error style (red ANSI color)

        Args:
            message (str): Message to print.
            tag (str): Prefix to print with the message. If `None` the default.
                tag for this kind of messages is used. An empty string will remove
                the tag for this print.
            bold (bool): `True` to use bright style to print the message (kind of bold font).
                By default `False`.
            highlight (bool): `True` to use the color on the background and a high contrast
                color for the message text.
            invert_color (bool): `True` to invert font color when highlight flag is on, this will
                switch between black and white. By default `False`. Hightlight font color white
        """
        if self._log_level > self._get_log_level_dict().get('error', self._max_verbosity):
            return

        print(self._get_error_str(message, *args, tag=tag, bold=bold, highlight=highlight, invert_color=invert_color))

    def _get_error_str(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        if tag is None:
            tag = self._error_tag

        style = Style.BRIGHT if bold else Style.NORMAL
        if highlight:
            style += "{}{}".format(Back.RED, Fore.WHITE if not invert_color and bold else Fore.BLACK)

        else:
            style += Fore.RED

        return self._get_decorated_str(message, *args, prefix=tag, style=style)

    def warning(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        """
        Prints a message to stdout with warning style (yellow ANSI color)

        Args:
            message (str): Message to print.
            tag (str): Prefix to print with the message. If `None` the default.
                tag for this kind of messages is used. An empty string will remove
                the tag for this print.
            bold (bool): `True` to use bright style to print the message (kind of bold font).
                By default `False`.
            highlight (bool): `True` to use the color on the background and a high contrast
                color for the message text.
            invert_color (bool): `True` to invert font color when highlight flag is on, this will
                switch between black and white. By default `False`. Hightlight font color white.
        """
        if self._log_level > self._get_log_level_dict().get('warning', self._max_verbosity):
            return
        
        print(self._get_warning_str(message, *args, tag=tag, bold=bold, highlight=highlight, invert_color=invert_color))

    def _get_warning_str(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        if tag is None:
            tag = self._warn_tag

        style = Style.BRIGHT if bold else Style.NORMAL
        if highlight:
            style += "{}{}".format(Back.YELLOW, Fore.BLACK if not invert_color and bold else Fore.WHITE)

        else:
            style += Fore.YELLOW

        return self._get_decorated_str(message, *args, prefix=tag, style=style)

    def info(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        """
        Prints a message to stdout with information style (cyan ANSI color)

        Args:
            message (str): Message to print.
            tag (str): Prefix to print with the message. If `None` the default.
                tag for this kind of messages is used. An empty string will remove
                the tag for this print.
            bold (bool): `True` to use bright style to print the message (kind of bold font).
                By default `False`.
            highlight (bool): `True` to use the color on the background and a high contrast
                color for the message text.
            invert_color (bool): `True` to invert font color when highlight flag is on, this will
                switch between black and white. By default `False`. Hightlight font color white.
        """
        if self._log_level > self._get_log_level_dict().get('info', self._max_verbosity):
            return

        print(self._get_info_str(message, *args, tag=tag, bold=bold, highlight=highlight, invert_color=invert_color))

    def _get_info_str(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        if tag is None:
            tag = self._info_tag

        style = Style.BRIGHT if bold else Style.NORMAL
        if highlight:
            style += "{}{}".format(Back.CYAN, Fore.WHITE if not invert_color and bold else Fore.BLACK)

        else:
            style += Fore.CYAN

        return self._get_decorated_str(message, *args, prefix=tag, style=style)

    def confirm(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        """
        Prints a message to stdout with confirmation style (green ANSI color)

        Args:
            message (str): Message to print.
            tag (str): Prefix to print with the message. If `None` the default.
                tag for this kind of messages is used. An empty string will remove
                the tag for this print.
            bold (bool): `True` to use bright style to print the message (kind of bold font).
                By default `False`.
            highlight (bool): `True` to use the color on the background and a high contrast
                color for the message text.
            invert_color (bool): `True` to invert font color when highlight flag is on, this will
                switch between black and white. By default `False`. Hightlight font color white.
        """
        if self._log_level > self._get_log_level_dict().get('confirm', self._max_verbosity):
            return

        print(self._get_confirm_str(message, *args, tag=tag, bold=bold, highlight=highlight, invert_color=invert_color))

    def _get_confirm_str(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        if tag is None:
            tag = self._confirm_tag

        style = Style.BRIGHT if bold else Style.NORMAL
        if highlight:
            style += "{}{}".format(Back.GREEN, Fore.WHITE if not invert_color and bold else Fore.BLACK)

        else:
            style += Fore.GREEN

        return self._get_decorated_str(message, *args, prefix=tag, style=style)

    def debug(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        """
        Prints a message to stdout with debug style (blue ANSI color)

        Args:
            message (str): Message to print.
            tag (str): Prefix to print with the message. If `None` the default.
                tag for this kind of messages is used. An empty string will remove
                the tag for this print.
            bold (bool): `True` to use bright style to print the message (kind of bold font).
                By default `False`.
            highlight (bool): `True` to use the color on the background and a high contrast
                color for the message text.
            invert_color (bool): `True` to invert font color when highlight flag is on, this will
                switch between black and white. By default `False`. Hightlight font color white.
        """
        if self._log_level > self._get_log_level_dict().get('debug', self._max_verbosity):
            return

        print(self._get_debug_str(message, *args, tag=tag, bold=bold, highlight=highlight, invert_color=invert_color))

    def _get_debug_str(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        if tag is None:
            tag = self._debug_tag

        style = Style.BRIGHT if bold else Style.NORMAL
        if highlight:
            style += "{}{}".format(Back.BLUE, Fore.WHITE if not invert_color and bold else Fore.BLACK)

        else:
            style += Fore.BLUE

        return self._get_decorated_str(message, *args, prefix=tag, style=style)

    def print(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        """
        Prints a message to stdout in with black and wihte palette.

        Args:
            message (str): Message to print.
            tag (str): Prefix to print with the message. If `None` the default.
                tag for this kind of messages is used. An empty string will remove
                the tag for this print.
            bold (bool): `True` to use bright style to print the message (kind of bold font).
                By default `False`.
            highlight (bool): `True` to use the color on the background and a high contrast
                color for the message text.
            invert_color (bool): `True` to invert font color when highlight flag is on, this will
                switch between black and white. By default `False`. Hightlight font color white.
        """
        if tag is None:
            tag = self.print_tag

        print(self._get_print_str(message, *args, tag=tag, bold=bold, highlight=highlight, invert_color=invert_color))

    def _get_print_str(self, message, *args, tag=None, bold=False, highlight=False, invert_color=False):
        style = Style.BRIGHT if bold else Style.NORMAL
        if highlight:
            style += "{}{}".format(Back.WHITE, Fore.BLACK if not invert_color else Fore.WHITE)

        else:
            style += Fore.WHITE

        return self._get_decorated_str(message, *args, prefix=tag, style=style)

    def _get_decorated_str(self, msg, *args, prefix='', style=None):
        clear_sty = Style.RESET_ALL
        if not style:
            clear_sty = ''
            style = ''

        if args:
            msg = msg.format(*args)

        return '{}{}{}{}'.format(style, prefix, msg, clear_sty)

    @property
    def log_level(self):
        """
        Current log level
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        self._log_level = self._get_log_level_id(log_level)

    @property
    def error_tag(self):
        """
        Default error messages tag
        """
        return self._error_tag

    @error_tag.setter
    def error_tag(self, new_tag):
        self._error_tag = str(new_tag)

    @property
    def warn_tag(self):
        """
        Default warning messages tag
        """
        return self._warn_tag

    @warn_tag.setter
    def warn_tag(self, new_tag):
        self._warn_tag = str(new_tag)

    @property
    def info_tag(self):
        """
        Default info messages tag
        """
        return self._info_tag

    @info_tag.setter
    def info_tag(self, new_tag):
        self._info_tag = str(new_tag)

    @property
    def confirm_tag(self):
        """
        Default confirmation messages tag
        """
        return self._confirm_tag

    @confirm_tag.setter
    def confirm_tag(self, new_tag):
        self._confirm_tag = str(new_tag)

    @property
    def debug_tag(self):
        """
        Default debuga messages tag
        """
        return self._debug_tag

    @debug_tag.setter
    def debug_tag(self, new_tag):
        self._debug_tag = str(new_tag)

    @property
    def print_tag(self):
        """
        Default standard messages tag
        """
        return self._print_tag

    @print_tag.setter
    def print_tag(self, new_tag):
        self._print_tag = str(new_tag)
