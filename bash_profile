ps -U root | grep logKextKiller.py > /dev/null
if [ $? -eq 0 ]; then
    echo “logging” # returns "logging" when terminal is opened
else
    sudo python /logKext/logKextKiller.py # The path to your logKextKiller.py file
fi
