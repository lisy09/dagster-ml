DBG_MAKEFILE ?=
ifeq ($(DBG_MAKEFILE),1)
    $(warning ***** starting Makefile for goal(s) "$(MAKECMDGOALS)")
    $(warning ***** $(shell date))
else
    MAKEFLAGS += -s
endif

SHELL := /usr/bin/env bash

# Define variables so help command work
PRINT_HELP ?=

# Noticed that this has impact when some command call in makefile call so need to be not enabled
# MAKEFLAGS += --no-builtin-rules

ROOT_DIR=${PWD}
DEV_TOOLS_DIR=${ROOT_DIR}/dev-tools
MAKEFILE_DIR=${DEV_TOOLS_DIR}/mkfiles
SCRIPT_DIR=${DEV_TOOLS_DIR}/scripts

include ${MAKEFILE_DIR}/*.mk