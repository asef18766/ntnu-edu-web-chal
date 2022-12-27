nohup su web -c "cd ~ && python3 service.py" > web.log 2> web.err &
nohup su dev -c "cd ~ && python3 dev_server.py" > dev.log 2> dev.err &
sleep 3
chmod 600 /dev/*
tail -f /dev/null