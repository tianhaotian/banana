#!/bin/bash

BANANA_HOME="$(cd `dirname "${BASH_SOURCE-$0}"`/..; pwd)"

export BANANA_HOME=BANANA_HOME
export LOGS=/app/logs/pandora
export CONF=BANANA_HOME/conf
export BIN=BANANA_HOME/bin
export PID=/app/logs/pandora
export LIB=BANANA_HOME/lib
export SRC=BANANA_HOME/src
export DATA=BANANA_HOME/data
export TEMPLATES=BANANA_HOME/templates
export SERVER=$SRC/server
export LOCALE=BANANA_HOME/locale
export TASK=$SRC/task
export SCRIPT=$SRC/script
export TEST_RESOURCE=BANANA_HOME/test/resource

export PYTHONPATH=$LIB:$LIB/pyhs2:$LIB/push:$LIB/dateutil:$SRC:$SRC/common/cloghandler
export PYTHON=python
export DATE=`date +"%Y-%m-%d"`