#!/bin/bash
python publisher.py "test/hello" "hello" 1 & python publisher.py "test/world" "world" 2 true
