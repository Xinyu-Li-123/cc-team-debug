#!/usr/bin/env bash
LOG_FILE=$1
ARGS_FILE=$2
cat $1 | grep -e "^* Wrong result for" | cut --delimiter " " -f5 >$2
echo "Found "$(wc -l $ARGS_FILE)" mismatched requests in total."
