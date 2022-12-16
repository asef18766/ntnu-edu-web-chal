nohup su web -c "cd ~ && python3 service.py" > web.log 2> web.err &
nohup python3 dev_server.py > dev.log 2> dev.err &
tail -f /dev/null