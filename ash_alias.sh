alias go='/bin/sh /root/iSH-scripts/menu.sh'
alias howto='cat /root/iSH-scripts/README'
alias rmkwh='ssh-keygen -f "/root/.ssh/known_hosts" -R $1'
alias telon='ssh-keygen -f "/root/.ssh/known_hosts" -R 192.168.1.1 ; ssh-keygen -f "/root/.ssh/known_hosts" -R 192.168.1.2 ; /bin/sh /root/iSH-scripts/telneton.sh | ssh admin@192.168.1.1 > /dev/null'
