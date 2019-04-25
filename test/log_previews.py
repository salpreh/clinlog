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
    log.print_error('Unable to access config file', bold=True)

    # Print warning highlighted and bold
    log.print_warn('The execution will continue with default configuration', None, True, True)

    # Confirmation log with provided tag
    log.print_confirm('Execution completed', '[SUCCESS]')


def error_tests(message, log):
    log.error_tag = '[BAD CALL] '
    log.print_error(message, '')
    log.print_error(message, '[ERROR] ', True)
    log.print_error(message, None, False, True)
    log.print_error(message, '[IMPORTANT] ', True, True)


def warn_tests(message, log):
    log.warn_tag = '[WARNING] '
    log.print_warn(message, '')
    log.print_warn(message, '[WARN] ', True)
    log.print_warn(message, None, False, True)
    log.print_warn(message, '[ATTENTION] ', True, True)


def info_tests(message, log):
    log.info_tag = '[INFO] '
    log.print_info(message, '')
    log.print_info(message, None, True)
    log.print_info(message, 'Remember: ', False, True)
    log.print_info(message, 'HEY: ', True, True)


def confirm_tests(message, log):
    log.print_confirm(message)
    log.print_confirm(message, '[OK] ', True)
    log.print_confirm(message, '[ACCEPTED] ', False, True)
    log.print_confirm(message, '[CONFIRMED] ', True, True)


def normal_print_tests(message, log):
    log.norm_tag = '[REGULAR] '
    log.print_norm(message, '')
    log.print_norm(message, None, True)
    log.print_norm(message, '', False, True)
    log.print_norm(message, '', True, True)


if __name__ == '__main__':
    sample_call()
    log = Logger()

    # Error preview
    msg = 'Notice this error!'
    log.print_norm('\nError messages', bold=True)
    print('='*len(msg))
    error_tests(msg, log)

    # Warn preview
    msg = 'Keep in mind this'
    log.print_norm('\nWarning messages', bold=True)
    print('='*len(msg))
    warn_tests(msg, log)

    # Info preview
    msg = 'You are in the right way'
    log.print_norm('\nInfo messages', bold=True)
    print('='*len(msg))
    info_tests(msg, log)

    # Confirm preview
    msg = 'That was absolutely right'
    log.print_norm('\nConfirmation messages', bold=True)
    print('='*len(msg))
    confirm_tests(msg, log)

    # Normal style preview
    msg = 'Pretty regular message'
    log.print_norm('\nNomal style messages', bold=True)
    print('='*len(msg))
    normal_print_tests(msg, log)
