#!/bin/bash

ssh_tag=$1
basepath=$(dirname $(cd `dirname $0`; pwd))
echo $basepath

for i in $(seq 1 30);do
    process_id=$(ps -ef | grep $ssh_tag| grep -v sshpass| grep -v grep| grep -v $0|awk '{print $2}')
    if [ ! -z $process_id ];then
        log_path=$basepath/log/`date +%F`
        mkdir -p $log_path
        echo "create log dir"
        sudo strace -fp $process_id -t -o $log_path/session_$2.log
        break;
    fi;
    sleep 1;
done;
