#!/bin/bash
sudo apt-get autoremove
sudo du -sh /var/cache/apt
sudo apt-get autoclean
sudo apt-get clean
sudo journalctl --vacuum-time=3d
rm -rf ~/.cache/thumbnails/*
