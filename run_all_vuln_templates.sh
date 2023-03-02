#!/bin/bash

BINARY=$1
TEMPLATE_DIR='vuln_templates'
LOG_DIR=$2

for FILE in $TEMPLATE_DIR/*.py; do
    FILE_NO_EXT=$(basename $FILE .py)
    BIN_NO_EXT=$(basename $BINARY)
    mkdir -p "$LOG_DIR/$BIN_NO_EXT"
    LOG_PATH="$LOG_DIR/$BIN_NO_EXT/${FILE_NO_EXT}_logs"
    JSON_PATH="$LOG_DIR/$BIN_NO_EXT/${FILE_NO_EXT}_json"
    OUTPUT_PATH="$LOG_DIR/$BIN_NO_EXT/${FILE_NO_EXT}_output.txt"
    echo "Starting $FILE_NO_EXT analysis..."
    python3 $TEMPLATE_DIR/run_arbiter.py -f $FILE -t $BINARY -l $LOG_PATH -j $JSON_PATH 2> $OUTPUT_PATH &
done