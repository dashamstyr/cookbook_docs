#!/bin/bash
rsync  --progress --stats -az /Users/phil/repos/feedback_papers/  -e ssh owlhome:/home/phil/public_html/Downloads/feedbacks/
