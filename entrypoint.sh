#!/bin/bash

set -e

# Nice to set this up for all future python code being run.
export PYTHONPATH="${PWD}/src"

#
# This execs whatever is provided as a COMMAND to the container. 
# This mechanism, though, allows us to run anything inside the container.
# Note that surrounding $@ with double quote causes the expansion (which starts with
# parameter 1 not 0) to result in each parameter being retained without splitting.
# Sort of like "$@" -> "$1" "$2" "$3" ..
#
exec "$@"
