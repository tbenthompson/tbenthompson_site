#!/usr/bin/python
import os
import sys
import datetime

def run(cmd):
    os.system(cmd)

folder_name = sys.argv[1]
post_name = sys.argv[2]

posts_folder = '/home/tbent/projects/tbenthompson_site/content/post'

run('jupyter nbconvert --to markdown %s/%s.ipynb' % (folder_name, folder_name))
run('cp -R %s %s' % (folder_name, posts_folder))
run('mv %s/%s/%s.md %s/' % (posts_folder, folder_name, folder_name, posts_folder))

md_file = '%s/%s.md' % (posts_folder, folder_name)

date_str = datetime.datetime.today().strftime('%Y-%m-%d')

prepend = """
+++
title="%s"
date=%s
+++
""" % (post_name, date_str)
with open(md_file, 'r') as f:
    file_str = f.read()
with open(md_file, "w") as f:
    f.write(prepend + file_str)
