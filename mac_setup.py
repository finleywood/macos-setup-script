#!/usr/bin/env python3
# Finley Wood 2024 (github.com/finleywood)
# MacOS setup script for setting up a new Mac with Homebrew, iTerm2, and neovim.


import os

print('Finley Wood\'s MacOS Setup Script')

print('Starting setup...')

# Install Rosetta 2
os.system('softwareupdate --install-rosetta --agree-to-license')

# Install Xcode Command Line Tools
os.system('xcode-select --install')

# Install Homebrew
os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')

# Install Homebrew packages
os.system('brew install git nvim tmux')

# Install iTerm2
os.system('brew install --cask iterm2')

# Install aliases
os.system('echo alias vim=nvim >> ~/.zshrc')

os.system('echo alias vi=nvim >> ~/.zshrc')

os.system('echo alias l=ls >> ~/.zshrc')

os.system('echo alias e=nvim >> ~/.zshrc')

# Clone and configure neovim

os.system('git clone https://github.com/finleywood/nvim-config.git ~/.config/nvim')

print('Remember to run :Copilot setup to finish setting up Copilot.')
print('Setup complete. Restart your terminal.')
