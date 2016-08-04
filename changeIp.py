#!/usr/bin/env python
print "Access-Control-Allow-Headers: Content-type,Status"
print "Content-Type: text/html; charset="
print "Access-Control-Allow-Origin: *"
print
import boto.ec2
import time

ec2_conn = boto.ec2.connect_to_region("us-west-2",aws_access_key_id="AKIAJJF3CQRQKAJ4OPRA", aws_secret_access_key="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")
instances = []
for reservation in ec2_conn.get_all_reservations():
	#reservation.instances returns a list of instances
	instances = instances + reservation.instances
for instance in instances:
	if instance.instance_type == "t2.micro":
		instance.stop()
		#returns stopping
		while instance.update()!="stopped":
		#	print instance.update()+" ip "+instance.ip_address
			time.sleep(4)
		instance.start()
		while instance.update()!="running":
		#	print instance.update()
			time.sleep(5)
		print instance.ip_address
