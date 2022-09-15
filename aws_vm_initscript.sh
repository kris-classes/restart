#!/bin/bash
# The purpose of this program is to auto install package on the aws virtual machine
# To install, run this: curl -s https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/aws_vm_initscript.sh | sh && exec zsh -l

# Setting color variables.
GREEN="\033[0;32m"
NC="\033[0m"

# Installing the cowsay package.
echo -e "\n[Installing cowsay...]\n"
sudo yum install cowsay -y && echo -e "${GREEN}Installed cowsay${NC}" | cowsay
echo

# Installing the epel repository.
echo Installing epel... | cowsay
echo
sudo amazon-linux-extras install epel && echo -e "\n${GREEN}[Installed epel]${NC}\n"

# This is a for loop that will install all the packages listed in the loop.
for package in git gcc zsh jq sl util-linux-user automake libevent-devel bison ncurses-devel
do
        echo Installing ${package}... | cowsay
        echo
        sudo yum install -y $package && echo -e "\n${GREEN}[Installed ${package}]${NC}\n"
done

# This is installing ohmyzsh.
echo Installing ohmyzsh... | cowsay
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && echo -e "\n${GREEN}[Installed ohmyzsh]${NC}\n"

# Downloading the .zshrc file from the github repository and placing it in the home directory.
echo Fetching zshrc config... | cowsay
curl https://raw.githubusercontent.com/Bugsbugme/unitec-aws-restart/main/data/.zshrc > $HOME/.zshrc && echo -e "\n${GREEN}[Retreived zshrc config]${NC}\n"

# Set ZSH_CUSTOM path
ZSH_CUSTOM=~/.oh-my-zsh/custom && echo -e "${GREEN}[Set ZSH_CUSTOM path]${NC}\n"

# This is downloading a ohmyzsh theme file from the github repository and placing it in the
# ZSH_CUSTOM/themes/ directory.
echo Fetching ohmyzsh theme... | cowsay
echo
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1 && echo -e "\n${GREEN}[Retreived ohmyzsh theme]${NC}\n"
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

# This is installing the zsh-autosuggestions plugin.
echo Installing zsh-autosuggestions... | cowsay
echo
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions && echo -e "\n${GREEN}[Installed zsh-autosuggestions]${NC}\n"

# This is changing the default shell to zsh.
sudo chsh -s $(which zsh) $(whoami)
echo

# Installing tldr.
echo Installing tldr... | cowsay
echo
sudo pip3 install tldr && echo -e "\n${GREEN}[Installed tldr]${NC}\n"

# This is installing rust.
echo Installing rust... | cowsay
echo
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > installrust.sh
chmod +x installrust.sh
./installrust.sh -y && echo -e "\n${GREEN}[Installed rust]${NC}\n"

# This is installing broot.
echo Installing broot... | cowsay
echo
mkdir $HOME/bin
curl https://dystroy.org/broot/download/x86_64-unknown-linux-gnu/broot > $HOME/bin/broot
chmod +x $HOME/bin/broot
broot --install && echo -e "\n${GREEN}[Installed broot]${NC}\n"

# This is installing tmux.
echo Installing tmux... | cowsay
echo
git clone https://github.com/tmux/tmux.git
cd tmux
sh autogen.sh
./configure
make
sudo make install && echo -e "\n${GREEN}[Installed tmux]${NC}\n"

# This is installing ohmytmux.
echo Installing ohmytmux... | cowsay
echo
cd $HOME
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local . && echo -e "\n${GREEN}[Installed ohmytmux]${NC}\n"

echo -e "${GREEN}Initialization complete, entering zsh...${NC}" | cowsay
echo