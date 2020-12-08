#!/usr/bin/env python

import boto3

# Connect to the Amazon EC2 service
ec2 = boto3.resource('ec2')

# Loop through each instance
for instance in ec2.instances.all():
  state = instance.state['Name']
  for tag in instance.tags:

    # Check for the 'stopinator' tag
    if tag['Key'] == 'stopinator':
      action = tag['Value'].lower()

      # Stop?
      if action == 'stop' and state == 'running':
        print "Stopping instance", instance.id
        instance.stop()

      # Terminate?
      elif action == 'terminate' and state != 'terminated':
        print "Terminating instance", instance.id
        instance.terminate()


'''
The script does the following:

Connects to the Amazon EC2 service
Obtains a list of all EC2 instances
Loops through each instance
If an instance is in the running state and has a tag named stopinator, it reads the value of the tag and then either stops or terminates the instance.
'''

'''
OTHER STOPINATOR IDEAS
Here are some ideas for implementing your own Stopinator:

Schedule the Stopinator to stop machines each evening, to save money.
Mark instances that you want to keep running, then have the Stopinator stop only unknown instances (but don’t terminate them – they might be important!).
Have another script that turns on the instances in the morning.
Set different actions for weekdays and weekends.
Use another tag to identify how many hours you want an instance to run, which is ideal for instances you just want to use for an experiments. Schedule the Stopinator to run hourly and configure it to terminate instances that run longer than the indicated number of hours.
''