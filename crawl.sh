#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR/bcra
. $DIR/bin/activate
mkdir out
rm out/*.json

scrapy crawl bcra_spider -o out/bcra.json -t json

