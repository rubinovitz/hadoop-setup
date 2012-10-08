tallation
===========

1. Download SSH, rsync, Java and [Hadoop](http://hadoop.apache.org/docs/r0.20.2/quickstart.html#Download "Title")

2. Extract Hadoop to usr/local/bin 

3.Add a hadoop user

	sudo addgroup hadoop
	sudo adduser --ingroup hadoop hduser

4. Configure SSH into hduser

	su - hduser
	hduser@ubuntu:~$ ssh-keygen -t rsa -P ""
	Generating public/private rsa key pair.
	Enter file in which to save the key (/home/hduser/.ssh/id_rsa):
	Created directory '/home/hduser/.ssh'.
	Your identification has been saved in /home/hduser/.ssh/id_rsa.
	Your public key has been saved in /home/hduser/.ssh/id_rsa.pub.
	The key fingerprint is:
	9b:82:ea:58:b4:e0:35:d7:ff:19:66:a6:ef:ae:0e:d2 hduser@ubuntu
	The key's randomart image is:
	[...snipp...]

5. Enable machine to act with key

	cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
