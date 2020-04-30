# Author : M.Daffa
# Team   : Black Coder Crush

# Open Source from other script

clear
echo
echo $cy"   ╔═══════════╗"
echo $cy" ╔═╝███████████╚═╗"
echo $cy"╔╝███████████████╚╗"
echo $cy"║█████████████████║"
echo $cy"║█████████████████║"
echo $cy"║█████████████████║"
echo $cy"║█╔█████████████╗█║"
echo $cy"╚╦╝███▒▒███▒▒███╚╦╝"
echo $cy"╔╝██▒▒▒▒███▒▒▒▒██╚╗"
echo $cy"║██▒▒▒▒▒███▒▒▒▒▒██║"
echo $cy"║██▒▒▒▒▒███▒▒▒▒▒██║"
echo $cy"║██▒▒▒▒█████▒▒▒▒██║"
echo $cy"╚╗███████████████╔╝"
echo $cy" ╚══╦╝██▒█▒██╚╦══╝"
echo $cy"    ║█████████║"
echo $cy"    ║█║██║██║█║"
echo $cy"    ╚═╩══╩══╩═╝"
echo $cy"["$me"1"$cy"]"$i" Install Metasploit "
echo $cy"["$me"2"$cy"]"$i" Kembali "
echo $bi"╭─# Metasploit Installer ["$bi"Masukkan pilihan anda"$bi"]"
read -p"╰───# Makky_2693 ~# " pil
if [ $pil = 1 ]
then
clear
pkg install wget
pkg install bash
pkg install root-repo
pkg install unstable-repo
pkg install x11-repo
bash fix-ruby-bigdecimal.sh.txt
wget https://github.com/termux/termux-packages/files/2912002/fix-ruby-bigdecimal.sh.txt
pkg install metasploit
fi
if [ $pil = 2 ]
then
clear
echo $cy"Semoga Bermanfaat"
sleep 1
echo $i"Jangan Lupa Share Tools Ini"
sleep 1
echo $pur"Dan Subscribe Channel Saya"
sleep 1
sleep 1
echo $pur"Terima kasih Yang Sudah Support dengan Tools ini"
sleep 1
clear
exit
fi