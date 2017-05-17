#!/bin/sh
parallel -j -1 -r --progress --xargs $@
