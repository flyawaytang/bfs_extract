#!/bin/bash

python3 ~/tools/bfs_extract/yank.py $1 stage1-$1
python3 ~/tools/bfs_extract/bfs.py stage1-$1 stage2-$1
python3 ~/tools/bfs_extract/bfs_extract.py stage2-$1 $2
