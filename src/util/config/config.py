#!/usr/bin/python
# encoding:utf-8
import os
from ConfigParser import RawConfigParser


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class Configuration:
    def __init__(self, config_file=None):
        base_name = os.getenv('USER') or 'app'
        dir_name = os.getenv('CONF') or 'conf'
        cus_name = os.getenv('CUS_CONF') or 'conf'
        default_conf = ["%s/%s.conf" % (dir_name, 'app'), "%s/%s.conf" % (dir_name, base_name),
                        "%s/%s.conf" % (cus_name, 'user')]
        self._config_file = default_conf if not config_file else config_file
        self._load()

    def _load(self):
        self._config = RawConfigParser()
        print "load config from : ", self._config_file
        self._config.read(self._config_file)

    def get(self, sect, opt):
        return self._config.get(sect, opt)

    def get_or_else(self, sect, opt, default):
        if self._config.has_option(sect, opt):
            return self._config.get(sect, opt)
        return default

    def get_section(self, section):
        if not self._config.has_section(section):
            return {}
        items = self._config.items(section)
        return dict(items)


def get(sect, opt):
    return Configuration().get(sect, opt)


def get_section(sect):
    return Configuration().get_section(sect)


def get_or_else(sect, opt, default):
    return Configuration().get_or_else(sect, opt, default)
