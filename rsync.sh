#!/bin/bash
rsync  --progress --stats -az /Users/phil/repos/cookbook_docs/  -e ssh owlhome:/home/phil/public_html/cookbook_docs

