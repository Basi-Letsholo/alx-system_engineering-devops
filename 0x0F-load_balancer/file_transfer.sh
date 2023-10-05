#!/usr/bin/env bash
# Transfers a file from client to server

arg_count=${#@}

if [ "$arg_count" -lt 3 ]; then
	echo "Usage: ./file_transfer.sh  PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
	exit 1
fi

file_to_transfer="$1"
IP="$2"
username="$3"
ssh_key="$4"

scp -o StrictHostKeyChecking=no -i "$ssh_key" "$file_to_transfer" "$username@$IP":~/
