ps -U root | grep logKextKiller.py > /dev/null
if [ $? -eq 0 ]; then
    echo “logging”
else
    sudo python /Applications/logKext/logKextKiller.py
fi
