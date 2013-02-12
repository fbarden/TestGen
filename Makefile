all:	view_send_cli.py

view_send_cli.py:	./view/send_cli.ui view_send_cli.patch
	pyuic4 -x ./view/send_cli.ui -o view_send_cli.py
	patch view_send_cli.py < view_send_cli.patch
