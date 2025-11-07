#!/bin/sh
export PYTHONPATH=/usr/app/utilities:$PYTHONPATH
echo "PYTHONPATH is set to: $PYTHONPATH"
ls /usr/app/utilities
python3.9 -c "import sys; print(sys.path)"
python3.9 -c "import utilities.PyAutoRunner"
python3.9 RunTest.py "$@"