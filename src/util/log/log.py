#!/usr/bin/python
# encoding:utf-8

import os
import logging
import logging.config
from util.http.request_context import HttpRequestContext

import util.config.config

this_path = os.path.dirname(os.path.abspath(__file__))
default_conf_path = "%s/../../../conf" % this_path
default_log_path = "%s/../../../logs" % this_path

conf_path = os.getenv("CONF", default_conf_path)
conf_file = "%s/logging.conf" % conf_path

logging.config.fileConfig(conf_file, defaults={"logpath": util.config.config.get('global', 'log_path')})
debug_enabled = int(util.config.config.get('global', 'enable_trace'))


def log_handler():
    """获取日志handler"""
    return logging.getLogger("pandora_cservice")


def runtime_log():
    return logging.getLogger("pandora_runtime")


def table_log():
    return logging.getLogger("table")


def adapter_log():
    return logging.getLogger('adapter')


def __trace_log_handler():
    return logging.getLogger("pandora_trace")


def trace_info(msg):
    if debug_enabled:
        log = __trace_log_handler()
        log.info(
            "[%s]\t[%s]" % (HttpRequestContext.data["trace_id"] if "trace_id" in HttpRequestContext.data else "", msg))


def trace_error(msg):
    if debug_enabled:
        log = __trace_log_handler()
        log.error(
            "[%s]\t[%s]" % (HttpRequestContext.data["trace_id"] if "trace_id" in HttpRequestContext.data else "", msg))
