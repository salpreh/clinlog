# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from clinlog import Logger


def sample_call():
    # Create the logger
    log = Logger()

    # Set default error message
    log.error_tag = '[ERROR]: '

    # Print error styled message
    log.error('Unable to access config file', bold=True)

    # Print warninging highlighted and bold
    log.warning('The execution will continue with default configuration', None, True, True)

    # Confirmation log with provided tag
    log.confirm('Execution completed', '[SUCCESS] ')

    # Confirmation log with provided tag
    log.debug('DB returned 8 entries for the user', '[DEBUG] ')


def error_tests(message, log):
    log.error_tag = '[BAD CALL] '
    log.error(message, '')
    log.error(message, '[ERROR] ', True)
    log.error(message, None, False, True)
    log.error(message, '[IMPORTANT] ', True, True)


def warning_tests(message, log):
    log.warning_tag = '[WARNING] '
    log.warning(message, '')
    log.warning(message, '[WARN] ', True)
    log.warning(message, None, False, True)
    log.warning(message, '[ATTENTION] ', True, True)


def info_tests(message, log):
    log.info_tag = '[INFO] '
    log.info(message, '')
    log.info(message, None, True)
    log.info(message, 'Remember: ', False, True)
    log.info(message, 'HEY: ', True, True)


def confirm_tests(message, log):
    log.confirm(message)
    log.confirm(message, '[OK] ', True)
    log.confirm(message, '[ACCEPTED] ', False, True)
    log.confirm(message, '[CONFIRMED] ', True, True)


def debug_tests(message, log):
    log.debug(message)
    log.debug(message, '[LOG] ', True)
    log.debug(message, '', False, True)
    log.debug(message, '[DEBUG] ', True, True)


def normal_tests(message, log):
    log.tag = '[REGULAR] '
    log.print(message, '')
    log.print(message, None, True)
    log.print(message, '', False, True)
    log.print(message, '', True, True)


if __name__ == '__main__':
    sample_call()
    log = Logger()

    # Error preview
    msg = 'Notice this error!'
    log.print('\nError messages', bold=True)
    print('='*len(msg))
    error_tests(msg, log)

    # Warn preview
    msg = 'Keep in mind this'
    log.print('\nWarning messages', bold=True)
    print('='*len(msg))
    warning_tests(msg, log)

    # Info preview
    msg = 'You are in the right way'
    log.print('\nInfo messages', bold=True)
    print('='*len(msg))
    info_tests(msg, log)

    # Confirm preview
    msg = 'That was absolutely right'
    log.print('\nConfirmation messages', bold=True)
    print('='*len(msg))
    confirm_tests(msg, log)

    # Confirm preview
    msg = 'DB retuned 5 entries'
    log.print('\nDebug messages', bold=True)
    print('='*len(msg))
    debug_tests(msg, log)

    # Normal style preview
    msg = 'Pretty regular message'
    log.print('\nNomal style messages', bold=True)
    print('='*len(msg))
    normal_tests(msg, log)
