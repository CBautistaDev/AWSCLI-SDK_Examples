# Overview
Amazon Web Services (AWS) is a collection of digital infrastructure services that developers can leverage when developing their applications. These services can be provisioned on-demand via multiple methods, such as automatically deploying services based on a schedule and intelligently responding to infrastructure events.

This lab demonstrates how to automate AWS by showing three way to access and manage AWS services:

AWS Management Console: This is a web application for managing Amazon Web Services. The console provides an intuitive user interface for performing many AWS tasks, such as working with Amazon S3 buckets, launching Amazon EC2 instances, and setting Amazon CloudWatch alarms.

AWS Command Line Interface (CLI): The AWS CLI is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

AWS Software Development Kit (SDK): AWS provides SDKs for numerous programming languages including Java, .NET, PHP, Go and Ruby. Using an SDK, you can build applications on top of Amazon S3 and Amazon EC2. This lab will use the SDK for the Python scripting language.

# TOPICS COVERED
This lab covers:

Using the AWS CLI to access and manage AWS services from the command line
Using the AWS SDK to programmatically access and manage AWS services
Configuring security for the AWS CLI
TECHNICAL KNOWLEDGE PREREQUISITES
Familiarity with command-line interfaces
A general understanding of scripting languages
Basic knowledge of AWS Services including Amazon EC2 and Amazon S3
# Start Lab
At the top of your screen, launch your lab by choosing Start lab
 You must wait for your AWS services to be ready before continuing.

Open your lab by choosing Open Console
This automatically logs you in to the AWS Management Console.

 Do not change the Region unless instructed.

COMMON LOGIN ERRORS
Error: You must first log out


If you see the message, You must first log out before logging into a different AWS account:

Choose here
Close your browser tab to return to your initial lab window
Choose Open Console again
# Task 1: Connect to your Linux EC2 instance
As part of this lab, a Linux EC2 Instance has been automatically created.

These instructions explain how to connect to the EC2 instance via SSH.

If you are using a Mac or Linux, skip to the next section.

 WINDOWS USERS: USING SSH TO CONNECT
 These instructions are for Windows users only.

To the left of the instructions you are currently reading, click  Download PPK.

Save the file to the directory of your choice.

You will use PuTTY to SSH to Amazon EC2 instances.

If you do not have PuTTY installed on your computer, <a href="https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe">download it here.

Open PuTTY.exe

Configure the PuTTY to not timeout:

Click Connection
Set Seconds between keepalives to 
30
This allows you to keep the PuTTY session open for a longer period of time.

Configure your PuTTY session:
Click Session
Host Name (or IP address): Copy and paste the PublicIP shown to the left of these instructions
In the Connection list, expand  SSH
Click Auth (don’t expand it)
Click Browse
Browse to and select the PPK file that you downloaded
Click Open to select it
Click Open
Click Yes, to trust the host and connect to it.
When prompted login as, enter: 
ec2-user
This will connect to your EC2 instance.

Windows Users: Click here to skip ahead to the next task.

## MAC  AND LINUX  USERS
These instructions are for Mac/Linux users only. If you are a Windows user, skip ahead to the next task.

To the left of the instructions you are currently reading, click  Download PEM.

Save the file to the directory of your choice.

Copy this command to a text editor:

```
chmod 400 KEYPAIR.pem

ssh -i KEYPAIR.pem ec2-user@PublicIP

```

Replace KEYPAIR.pem with the path to the PEM file you downloaded.

Replace EPublicIP with the value of PublicIP shown to the left of these instructions.

Paste the command into the Terminal window and run it.

Type 
yes
 when prompted to allow a first connection to this remote SSH server.

Because you are using a key pair for authentication, you will not be prompted for a password.


# Task 2: Three Ways to Access AWS
In this task, you will discover how to access AWS services using three different methods:

AWS Management Console
AWS Command Line Interface (CLI)
Programmatically using the Python SDK
To demonstrate how each access method operates, you will be using each of these methods to create an Amazon EC2 Key Pair, which is a public-private pair of encryption keys used to access Amazon EC2 instances.

CREATE A KEY PAIR USING THE AWS MANAGEMENT CONSOLE
In the AWS Management Console on the Services  menu, click EC2.

In the left navigation pane, click Key Pairs.

One existing Key Pair will be displayed. This is the Key Pair you used to access your Amazon EC2 instance.

You will now create a new Key Pair using the AWS Management Console.

Click Create key pair and configure:
Key pair name: 
console
File format:
If you are using Windows, select ppk.
If you are using MAC/Linux, select pem.
Click Create key pair
The console will then download a file that contains your Private Key.

This is just one way to create a Key Pair.

CREATE A KEY PAIR USING THE CLI
You will now create a Key Pair with the AWS Command Line Interface (CLI).

Return to the PuTTY/SSH window.

Paste this command in your PuTTY/SSH window:

```
aws ec2 create-key-pair --key-name CLI
```
A large block of text will appear with your RSA Private Key. You would normally store this key for future use, but it is not required for this lab.

This command created a Key Pair just like the console. However, the AWS CLI gives the ability to interface with AWS without having to click through a web page.

CREATE A KEY PAIR PROGRAMMATICALLY
It is also possible to interact with AWS services from a programming language or scripting language. This adds the ability to perform logic around AWS, such as obtaining a list of Amazon EC2 instances, then performing an action against each instance.

A small program has been provided that will create a Key Pair using the Python scripting language.

Paste this command to view the script:
```
cat create-keypair.py

```
The script does the following:

Loads the AWS SDK for Python, called boto
Connects to the Amazon EC2 service
Creates a Key Pair called SDK
Displays the Key Pair on-screen (this normally would be saved to a file)
Paste this command to run the script:

./create-keypair.py
A new RSA Private Key fingerprint will be displayed and a Key Pair will be created in the AWS EC2 service.

Return to the web browser showing the EC2 management console.

Click  Refresh.

The console now displays the keypairs created via the console, the CLI and the SDK.

This has provided a quick example of how the same operation (in this case, creating a Key Pair) can be done in the Management Console, the CLI and programmatically with an SDK.

AUTOMATICALLY CLEANUP
Scripts can also be used to cleanup unwanted resources. A script has been provided that will remove Key Pairs created during this lab.

Paste this command into your SSH/PuTTY window to view the script:

cat cleanup-keypairs.py
The script does the following:

Connects to the Amazon EC2 service
Obtains a list of all Key Pairs
Deletes all Key Pairs except for the one with ‘lab’ in the name
Paste this command to run the script:

./cleanup-keypairs.py
A list of deleted Key Pairs will be displayed.

Return to the Management Console and click  Refresh.
You will notice that the Key Pairs you created have been removed from the list.

These types of scripts can also be scheduled to run automatically to perform cleanup operations each night on AWS. You now know how to automate your infrastructure!

 # Task 3: Access Amazon S3 with the AWS CLI
The AWS CLI provides convenient commands for accessing Amazon S3. Here are some of the available commands:

Command	Purpose
Make a bucket	
```aws s3 mb s3://my-bucket```
List all buckets	
```aws s3 ls```
List the contents of a specific bucket	
```aws s3 ls s3://my-bucket```
Upload a file to a bucket	
```aws s3 cp file s3://my-bucket/file```
Download a file from a bucket	
```aws s3 cp s3://my-bucket/file file```
Copy a file between buckets	
aws s3 cp s3://bucket1/file s3://bucket2/file
Synchronize a directory with an S3 bucket	
```aws s3 sync my-directory s3://my-bucket/```
You will now create a bucket, which is used by Amazon S3 to store objects.

Each Amazon S3 bucket requires a unique name, so you will add a random number to the name of the bucket.

Create a bucket with this command (replacing 123 with a random number):

```aws s3 mb s3://data-123```
 If you receive an error that The requested bucket name is not available, try again with a different number.

You can now view your bucket in the S3 Management Console.

Return to the AWS Management Console. On the Services  menu, click S3.

Click the name of your data- bucket.

The bucket is currently empty. You will now copy some files to the bucket using the AWS CLI.

Paste this command into the PuTTY/SSH window to copy a file to your Amazon S3 bucket:
(Be sure to change data-123 to your bucket name!)


```aws s3 cp create-keypair.py s3://data-123```
The command copies the create-keypair.py file to the Amazon S3 bucket.

In the Management Console, click  Refresh.
The file should now be listed in your bucket.

You can also list the contents of a bucket from the CLI:

View the contents of your bucket with this command:
(Be sure to change data-123 to your bucket name!)


```aws s3 ls s3://data-123```
The AWS CLI command includes a Sychronize command that recursively copies new and updated files from the source directory to the destination. This is an excellent way to backup data to the cloud.

Paste this command to synchronize files to Amazon S3:
(Be sure to change data-123 to your bucket name!)


aws s3 sync . s3://data-123
You can view the list of files in the Amazon S3 Management Console.

In the Management Console, click  Refresh.
Many synchronized files should now appear.

The sync command only copies files that are not in the destination, or any files that have changed since the last time sync was run. This makes it easy to perform an incremental backup to Amazon S3.

AUTOMATING AMAZON S3
As seen from these examples, the AWS CLI is a convenient way to move data to/from Amazon S3.

The AWS CLI can be installed on any computer, not just an Amazon EC2 instance. Therefore, the CLI could be used for activities such as:

Sending backups to the cloud
Providing shared access to documents from multiple computers
Retrieving scripts and application code from a central repository
Duplicating data between different regions
The commands can be easily stored in a script file and set to operate at a scheduled time by using a cron command (Linux) or a Scheduled Task (Windows).

Task 4: Automate EBS Snapshots
Amazon Elastic Block Store (Amazon EBS) provides block level storage volumes for use with Amazon EC2 instances.

Amazon EBS Snapshots are an easy way to backup data stored on an Amazon EBS Volume. If the volume fails, or data is accidentally deleted, the snapshot can be used to create a new volume. Therefore, it is advisable to frequently take a snapshot of important volumes.

Once again, snapshots can be created in three ways:

Via the Management Console
Via the AWS CLI
Programmatically
CREATE AN EBS SNAPSHOT IN THE MANAGEMENT CONSOLE
First, you will take a snapshot manually and learn how to automate the task.

In the AWS Management Console on the Services  menu, click EC2.

In the left navigation pane, click Volumes.

Select  the 20 GiB volume.

This volume is attached to a Test Instance.

You will now create a snapshot of the volume.

Click Actions  and select Create Snapshot, then configure:
Description: 
Console Snapshot
Click Create Snapshot
Click Close
In the left navigation pane, click Snapshots.
Your Console Snapshot will appear in the list. It will start in the pending state, and will move to the completed state once the snapshot has been fully captured.

CREATE AN EBS SNAPSHOT WITH THE AWS CLI
To create a snapshot of a volume via the AWS CLI, you will first need to copy the ID of the Volume.

In the left navigation pane, click Volumes.

Select  the 20 GiB volume.

In the lower half of the screen, copy the Volume ID to your clipboard.

The Volume ID will look similar to: vol-021654b5f7cd631dc

Tip: If you hover over the Volume ID, a copy  icon will appear. Click the icon to copy the displayed value.

Type the following command in your ssh window, replacing YOUR-VOLUME-ID with the Volume ID you just copied:

aws ec2 create-snapshot --description CLI --volume-id YOUR-VOLUME-ID
Information will be displayed, indicating that your snapshot is pending.

In the Management Console, in the left navigation pane, click Snapshots.
You should see a new snapshot in the list with a Description of CLI. This snapshot will be completed quickly because snapshots are incremental and no data has changed on your volume since the last snapshot.

Snapshot creation can be easily automated with the AWS CLI by using a cron command (Linux) or a Scheduled Task (Windows).

CREATE AN EBS SNAPSHOT PROGRAMMATICALLY
Using a program or script to manage AWS resources allows the addition of logic that can modify operations based on existing conditions. For example, to control the number of snapshots that should be retained.

Each time a Create Snapshot command is issued, another snapshot is created. This means you will accumulate many snapshots, but you might only want to keep a few recent snapshots. The best way to achieve this is with a script that removes old snapshots.

A script has been provided that does exactly this!

View the script by typing the following command in your ssh session.

cat snapshotter.py
The script does the following:

Connects to the Amazon EC2 service
Goes through list of all EBS volumes and for each volume:
Creates a new snapshot
Obtains a list of snapshots for that volume
Deletes the oldest snapshots, leaving the two most recent snapshots
Run the script by typing the following command:

./snapshotter.py
In the Management Console, click  Refresh.
You should see two 20 GiB snapshots of the Test Instance and one 8 GiB snapshot of the CLI instance.

Check that it is rotating correctly:
Make a mental note of the snapshots displayed
Run the snapshotter.py command again
Refresh  the console
You should see that two new snapshots have been created and an old snapshot has disappeared. The snapshotter script will always keep the latest two snapshots for each volume.

Another method for rotating snapshots is to use the Amazon Data Lifecycle Manager, which provides the capability built-into the Amazon EC2 service.

Task 5: Automate Bastion Security
A Bastion host (also known as a Jump Box) is a computer on a network specifically designed and configured to withstand attacks. The bastion generally hosts a single application, for example a proxy server, and all other services are removed or limited to reduce potential threats to the computer.

Users of Amazon EC2 often implement a Bastion host to enable ssh (Linux) or Remote Desktop (Windows) access to other servers. Those other servers will only accept incoming connections from the Bastion host, thereby improving security.



Security can be further improved by limiting the range of IP Addresses that are allowed to connect to the Bastion host. The best way to do this is to open access only when required, and to remove access when not required. To assist with this, the AWS CLI can be used to grant and revoke security access.

CREATE A SECURITY GROUP
The first step is to create a Security Group that will be associated with the Bastion host.

In the left navigation pane, click Security Groups.

Click Create security group and configure:

Security group name: 
Bastion
Description: 
Bastion
VPC: Lab VPC
Click Create security group
This will create an empty Security Group that, by default, prohibits all incoming traffic.

PERMIT INBOUND TRAFFIC
You will now configure the Security Group to allow inbound traffic from your current Public IP Address.

Return to your ssh session and enter this command (all on a single line) to obtain the Security Group ID:

SECURITY_GROUP_ID=`aws ec2 describe-security-groups --filters Name=group-name,Values=Bastion --query SecurityGroups[*].GroupId --output text`
This command obtains the ID of the Security Group and stores it in a variable.

Open this link to discover your public IP address: http://checkip.amazonaws.com/

Return to your ssh session and enter this command (all on a single line), replacing YOUR-PUBLIC-IP-ADDRESS with your public IP address and keeping the 
/32
 at the end:


aws ec2 authorize-security-group-ingress --group-id $SECURITY_GROUP_ID --protocol tcp --port 22 --cidr YOUR-PUBLIC-IP-ADDRESS/32
This has now added a rule to the Bastion security group.

In the Management Console, click the Inbound tab in the lower pane.

Click  Refresh in the top-right of the page.

You should see the permission that was added for SSH access.

Access can also be revoked via the AWS CLI.

Return to your ssh session and enter this command (the only change is that authorize is now revoke).

aws ec2 revoke-security-group-ingress --group-id $SECURITY_GROUP_ID --protocol tcp --port 22 --cidr YOUR-PUBLIC-IP-ADDRESS/32
Click  Refresh in the AWS Management Console.
The permission should have disappeared.

AUTOMATE THE GRANTING OF INBOUND ACCESS
Obtaining your Public IP address each time access is desired can become laborious. Fortunately, a script can do this for you!

View the script:

cat bastion-open
The script does the following:

Retrieves the Public IP address of the instance from checkip.amazonaws.com
Adds the IP address to the bastion Security Group
Run the script:

./bastion-open
Refresh  the AWS Management Console to confirm that access was granted.
In this case, the IP address of the Amazon EC2 instance was added. If you ran this type of command from your own computer, it would add the IP address of your computer (or of your corporate network).

REVOKE ALL ACCESS VIA A SCRIPT
Revoking access can also be scripted, but it may be necessary to remove ALL existing IP Addresses rather than just your current IP address. This is made easier by using a Python script.

View the Python script:

cat bastion-close.py
The script does the following:

Connects to the Amazon EC2 service
Retrieves the Security Group named Bastion
Deletes all the rules associated with the Security Group
Run the script:

./bastion-close.py
Click  Refresh in the AWS Management Console.
All rules in the Security Group should now have been deleted.

Task 6: Control Amazon EC2 Instances with The Stopinator!
Amazon EC2 incurs a charge for every hour that an instance is running. Therefore, the easiest way to save money is to turn off instances that are not required.

INTRODUCING - THE STOPINATOR!
The Stopinator is a simple script that turns off Amazon EC2 instances. It can be triggered by cron (Linux) or a Scheduled Task (Windows) and if it finds instances that have a specific tag, it either stops or terminates them.

In the left navigation pane, click Instances.
You will notice that a Test Instance has been provided. You will use the Stopinator to automatically stop this instance.

View the Stopinator script in your SSH session:

cat stopinator.py
The script does the following:

Connects to the Amazon EC2 service
Obtains a list of all EC2 instances
Loops through each instance
If an instance is in the running state and has a tag named stopinator, it reads the value of the tag and then either stops or terminates the instance.
Run the script:

./stopinator.py
Return to the AWS Management Console.

In the left navigation pane, click Instances.

Check the Instance State column to view the state of your Test instance.

Nothing has stopped! That’s right – the Stopinator did not stop the instance. Why? The Stopinator script only stops instances that have a stopinator tag. None of your Amazon EC2 instances currently have this tag, so they were not affected. This is a feature of the Stopinator so that it does not accidentally stop incorrect instances.

You can now add a stopinator tag to your instance with the following steps:

Select  Test instance.

Click the Tags tab at the bottom of the screen.

Click Manage tags

Click Add tag and configure:

Key: 
stopinator
 (be sure to spell it correctly, and in lowercase!)
Value: 
stop
Click Save
Run the Stopinator script again:

./stopinator.py
In the EC2 management console, click  Refresh.
Your test instance should now be in a stopping or stopped state.

Modify your tag to cause the Stopinator to terminate the test instance:
Click Add/Edit Tags
Change the Value from stop to: 
terminate
Click Save
Run the Stopinator script again:

./stopinator.py
In the EC2 management console, click  Refresh.
Your instance should now be in a shutting-down or terminated state.

OTHER STOPINATOR IDEAS
Here are some ideas for implementing your own Stopinator:

Schedule the Stopinator to stop machines each evening, to save money.
Mark instances that you want to keep running, then have the Stopinator stop only unknown instances (but don’t terminate them – they might be important!).
Have another script that turns on the instances in the morning.
Set different actions for weekdays and weekends.
Use another tag to identify how many hours you want an instance to run, which is ideal for instances you just want to use for an experiments. Schedule the Stopinator to run hourly and configure it to terminate instances that run longer than the indicated number of hours.
Task 7: Custom CloudWatch Metrics
Amazon CloudWatch monitors your AWS resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are the variables you want to measure for your resources and applications.

In addition to monitoring the built-in metrics that come with AWS, you can monitor your own custom metrics. This allows CloudWatch to react to any unusual situation in your own application.

CloudWatch metrics remain visible for 15 months, so your CloudWatch service might show metrics from previous lab users. This is expected behavior.

SENDING METRICS VIA THE AWS CLI
A custom metric can be sent to CloudWatch from the AWS CLI. In the example below, you will send a custom metric to CloudWatch. The metric has several attributes:

Namespace: The general category for your metric (eg, ERP)
Metric name: The name of the specific metric. For this lab, use your initials so you can identify your own metrics.
Value: The value associated with your metric
Timestamp: This is automatically assigned to the metric when it is sent to CloudWatch.
Run the following command in your ssh session, replacing YOUR_INITIALS with your own initials to make a unique metric:

aws cloudwatch put-metric-data --namespace Lab --metric-name YOUR-INITIALS --value 42
In the AWS Management Console on the Services  menu, click CloudWatch.

In the left navigation pane, click Metrics.

Under Custom Namespaces, click the Lab heading.

Click Metrics with no dimensions.

Select  the metric with your initials.

The graph should show your metric with a dot at 42 on the chart.

 It might take some time for your metric to appear, so click Refresh  every 30 seconds.

GENERATING MORE METRICS
One data point is not very exciting, so your next task is to generate more metrics. Rather than doing it manually, you now have an opportunity to play the classic High-Low game!

A script has been provided to play several High-Low games with you. The script will generate a number from 1 to 100 and your job is to guess that number. After each guess, you’ll be told if your guess is Too High or Too Low. Once you successfully guess the number, the script will send a metric to CloudWatch with the number of seconds it took you to play the game.

Play the game for several rounds and then visit CloudWatch to view your metrics.

Start the game by running the following command in your ssh session:

./highlow.py
Play the game several times to generate some metrics. Metrics are averaged over a period of time, so spread your game-playing over several minutes to collect more data.

Return to the CloudWatch Console in your web browser and refresh the web page to cause the new metric to appear.

Deselect the metric with your initials and select  highlow.

Click custom at the top of the page and select 1 minute.

You should see one or more summarized metrics showing the time it took for you to guess the numbers.

You are welcome to examine the code in the highlow.py script.

Task 8: Security Credentials for your Scripts
While performing the steps in this lab, you may have noticed that there was no prompt for security credentials. You were able to copy data, take snapshots and stop instances without having to identify yourself. Does this mean, therefore, that anybody could access your data and control your systems without permission?

Fortunately, your systems are kept secure. This lab was created to make it easy for you to execute commands in three methods: in the console, in the AWS CLI and programmatically. It is worth understanding how this was done, so that you can manage security in your own environment.

INSTANCE METADATA SERVICE
Instance metadata is data about your instance that you can use to configure or manage the running instance. Included in the data is a set of security credentials that was used for all your commands during this lab.

It works as follows:

A role called scripts was created with appropriate permissions to run the lab.
The Amazon EC2 instance you have been using was launched with the scripts role.
The AWS CLI and Python SDK automatically retrieved the security credentials via the Instance Metadata Service.
You can also view the security credentials by calling the Instance Metadata Service.

Run the following command in your ssh session:

./show-credentials
A large block of text will appear, similar to this:


{
 "Code" : "Success",
 "LastUpdated" : "2018-09-25T02:56:23Z",
 "Type" : "AWS-HMAC",
 "AccessKeyId" : "ASIAIXV6JMDVBZ7UJ2AA",
 "SecretAccessKey" : "zKxP9oe1cF/+p9KbexampleGu/smISHT6ZsO",
 "Token" : "examplebdcKLcAsGTSkQz2EIrSZtUWp8heRT/wSO"
 "Expiration" : "2018-09-25T08:59:36Z"
 }
The metadata contains an Access Key and Secret Key, which authorizes the AWS CLI and scripts on your EC2 instance to call AWS services.

USING THE AWS CLI ON OTHER COMPUTERS
The AWS CLI can be installed on any computer.

It is available for download from: http://aws.amazon.com/cli

However, when you run the AWS CLI on your own computer, it will not have access to security credentials from the Instance Metadata Service (which is only available from Amazon EC2 instances).

There are several alternative methods of providing security credentials to the AWS CLI:

Setting Environment Variables: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
Storing a local credentials file
Further details are available in the following documentation: boto3 Credentials]

Task 9: Accessing Help and Documentation
The AWS CLI includes an in-built help function.

Try these commands to display HELP information, pressing ‘Q’ to quit after each command:

aws help

aws ec2 help

aws ec2 describe-instances help
The complete documentation for the AWS CLI is available at: boto3 Documentation

SCRIPTING AND SDK DOCUMENTATION
Software Development Kits (SDKs) are available for several languages:

C++
Go
Java
JavaScript and node.js
.NET
PHP
Python
Ruby
(and others via community support)
These SDKs make it easy for your own software to interact with AWS. They also automatically retrieve Security Credentials via the Instance Metadata Service when running on EC2 instances.

Documentation for the SDKs is available at: SDKs and Tookits

Conclusion
 Congratulations! You have successfully completed this lab and learned how to:

Use the AWS CLI to access and manage AWS services from the command line
Use the AWS SDK to programmatically access and manage AWS services
Configure security for the AWS CLI
End Lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

On the navigation bar, choose AWSLabsUser, and then choose Sign Out.

Choose End lab and then confirm that you want to end your lab.