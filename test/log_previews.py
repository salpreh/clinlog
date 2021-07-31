# -*- coding: utf-8 -*-
import sys
import os
import logging
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

from clinlog import Logger
from clinlog.logging import ClinlogHandler
from clinlog.logging import get_logger as get_clinlog_logger


def error_tests(message, log):
    log.error_tag = '[BAD CALL] '
    log.error(message, tag='')
    log.error(message, tag='[ERROR] ', bold=True)
    log.error(message, tag=None, bold=False, highlight=True)
    log.error(message, tag='[IMPORTANT] ', bold=True, highlight=True)


def warning_tests(message, log):
    log.warning_tag = '[WARNING] '
    log.warning(message, tag='')
    log.warning(message, tag='[WARN] ', bold=True)
    log.warning(message, tag=None, bold=False, highlight=True)
    log.warning(message, tag='[ATTENTION] ', bold=True, highlight=True)


def info_tests(message, log):
    log.info_tag = '[INFO] '
    log.info(message, tag='')
    log.info(message, tag=None, bold=True)
    log.info(message, 'Remember: ', bold=False, highlight=True)
    log.info(message, tag='HEY: ', bold=True, highlight=True)


def confirm_tests(message, log):
    log.confirm(message)
    log.confirm(message, tag='[OK] ', bold=True)
    log.confirm(message, tag='[ACCEPTED] ', bold=False, highlight=True)
    log.confirm(message, tag='[CONFIRMED] ', bold=True, highlight=True)


def debug_tests(message, log):
    log.debug(message)
    log.debug(message, tag='[LOG] ', bold=True)
    log.debug(message, tag='', bold=False, highlight=True)
    log.debug(message, tag='[DEBUG] ', bold=True, highlight=True)


def normal_tests(message, log):
    log.tag = '[REGULAR] '
    log.print(message, tag='')
    log.print(message, tag=None, bold=True)
    log.print(message, tag='', bold=False, highlight=True)
    log.print(message, tag='', bold=True, highlight=True)


def logging_preview():
    logger = logging.getLogger('clinlog')
    cl_handler = ClinlogHandler()
    
    logger.setLevel(logging.DEBUG)
    logger.addHandler(cl_handler)

    logger.critical('This is a critical error!')
    logger.error('This is an error')
    logger.warning('Some warning')
    logger.info('Everithing is going right for now')
    logger.debug('User input was 4')

def logging_create_preview():
    logger = get_clinlog_logger(logging.DEBUG)

    logger.critical('This is a critical error!')
    logger.error('This is an error')
    logger.warning('Some warning')
    logger.info('Everithing is going right for now')
    logger.debug('User input was 4')

def sample_preview():
    # Create the logger
    log = Logger()

    # Set default error message
    log.error_tag = '[ERROR]: '

    # Print error styled message
    log.error('Unable to access config file', bold=True)

    # Print warninging highlighted and bold
    log.warning('The execution will continue with default configuration', tag=None, bold=True, highlight=True)

    # Confirmation log with provided tag
    log.confirm('Execution completed', '[SUCCESS] ')

    # Confirmation log with provided tag
    log.debug('DB returned 8 entries for the user', '[DEBUG] ')


def clinlog_preview():
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

if __name__ == '__main__':
    # sample_preview()
    clinlog_preview()
    logging_preview()
    logging_create_preview()
