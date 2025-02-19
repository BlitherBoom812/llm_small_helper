
export HOSTIP=$(cat /etc/resolv.conf | grep "nameserver" | cut -f 2 -d " ")
export HOSTPORT=12000
# HOSTIP=127.0.0.1

export http_proxy="http://$HOSTIP:$HOSTPORT"

export https_proxy="http://$HOSTIP:$HOSTPORT"

# export all_proxy="socks5://$HOSTIP:$HOSTPORT"

# export ALL_PROXY="socks5://$HOSTIP:$HOSTPORT"

git config --global https.proxy $https_proxy

git config --global http.proxy $http_proxy

alias pip="pip --proxy $http_proxy"
