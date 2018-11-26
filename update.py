import git
import os

reboot_cmd = 'sudo reboot'
git_dir = "/home/pi/serversidepi"

g = git.cmd.Git(git_dir)
g.pull()

os.system(reboot_cmd)
