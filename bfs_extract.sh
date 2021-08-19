#!/bin/bash

python3 ./yank.py $1 stage1-$1
python3 ./bfs.py stage1-$1 stage2-$1
python3 ./bfs_extract.py stage2-$1 $2
