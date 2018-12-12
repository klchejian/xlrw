#ps -ef|grep zbarcam|grep -v 'grep zbarcam'|awk '{print $2}'|xargs kill -9
clear;
python /home/chejian/xlrw/qrscan.py
