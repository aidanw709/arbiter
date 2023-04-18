#!/bin/bash

# This script runs all of the vulnerability templates in vuln_templates
# The only inputs are a path to the binary and a directory to dump the logs
#
#
# The log directory will have new paths implemented. A directory will be created
# with the binary name and then a new directory for each CWE. 
#
# Tree view:
# log_dir
#   |
#   |-- binary_name
#       |
#       |-- CWE###
#           |
#           |-- log files
#
# Example Command
# ./run_all_vuln_templates.sh path/to/binary logs
#


BINARY=$1
TEMPLATE_DIR='vuln_templates'
LOG_DIR=$2

for FILE in $TEMPLATE_DIR/*.py; do
    FILE_NO_EXT=$(basename $FILE .py)
    BIN_NO_EXT=$(basename $BINARY)
    mkdir -p "$LOG_DIR/$BIN_NO_EXT/${FILE_NO_EXT}"
    LOG_PATH="$LOG_DIR/$BIN_NO_EXT/${FILE_NO_EXT}"
    JSON_PATH="$LOG_DIR/$BIN_NO_EXT/${FILE_NO_EXT}"
    OUTPUT_PATH="$LOG_DIR/$BIN_NO_EXT/${FILE_NO_EXT}/output.txt"
    echo "Starting $FILE_NO_EXT analysis..."
    python3 $TEMPLATE_DIR/run_arbiter.py -f $FILE -t $BINARY -l $LOG_PATH -j $JSON_PATH 2> $OUTPUT_PATH &
done
wait

mv ArbiterReport_* "$LOG_DIR/$BIN_NO_EXT"