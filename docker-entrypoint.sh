#!/bin/bash

#!/bin/bash

echo ""
echo ""

APP="/app/app.py"           
CONFIG="/app/settings.py" 

# Validate parameters
#if [ -z "$DEVICE" ]; then
#    echo "Missing: Printer device (/dev/ttyusb0). Use '-e DEVICE=<device>'"
#    exit 1
#fi

#echo "Slack token: $DEVICE"
#echo ""

# Update settings
#sed -i "s/<slack_token>/$SLACK_TOKEN/" $CONFIG
#sed -i "s/<slack_channel>/$SLACK_CHANNEL/" $CONFIG
#sed -i "s,<slack_icon_url>,$SLACK_ICON_URL," $CONFIG
#sed -i "s/<slack_user_name>/$SLACK_USER_NAME/" $CONFIG

# Hand off to the CMD
exec "$@"