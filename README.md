Installation
===========

1. Download SSH, rsync, Java and [Hadoop](http://hadoop.apache.org/docs/r0.20.2/quickstart.html#Download "Title")

2. Extract Hadoop to usr/local/hadoop

3. Add a hadoop user

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

6. Disable IPv6 for Hadoop
	export HADOOP_OPTS=-Djava.net.preferIPv4Stack=true


7. Make sure the hadoop user, hduser, owns hadoop
	sudo chown -R hduser:hadoop hadoop

8. Update $HOME/.bashrc

					# Set Hadoop-related environment variables
				export HADOOP_HOME=/usr/local/hadoop

				# Set JAVA_HOME (we will also configure JAVA_HOME directly for Hadoop later on)
				export JAVA_HOME=/usr/lib/jvm/java-6-sun

				# Some convenient aliases and functions for running Hadoop-related commands
				unalias fs &> /dev/null
				alias fs="hadoop fs"
				unalias hls &> /dev/null
				alias hls="fs -ls"

				# If you have LZO compression enabled in your Hadoop cluster and
				# compress job outputs with LZOP (not covered in this tutorial):
				# Conveniently inspect an LZOP compressed file from the command
				# line; run via:
				#
				# $ lzohead /hdfs/path/to/lzop/compressed/file.lzo
				#
				# Requires installed 'lzop' command.
				#
				lzohead () {
						hadoop fs -cat $1 | lzop -dc | head -1000 | less
				}

				# Add Hadoop bin/ directory to PATH
				export PATH=$PATH:$HADOOP_HOME/bin

9. Update hadoop-env.sh


