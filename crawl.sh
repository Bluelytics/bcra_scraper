#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


cd $DIR
. $DIR/bin/activate
mkdir out
rm out/*.json
cd bcra

scrapy crawl bcra_spider -o ../out/bcra.json -t json
cd ..
Rscript analyze.R
../bluelytics/update_bcra.sh
