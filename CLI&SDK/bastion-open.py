IP =`curl - s checkip.amazonaws.com`
SECURITY_GROUP_ID =`aws ec2 describe-security-groups - -filters Name = group-name, Values = Bastion - -query SecurityGroups[*].GroupId - -output text`
aws ec2 authorize-security-group-ingress - -group-id $SECURITY_GROUP_ID - -protocol tcp - -port 22 - -cidr $IP/32


'''
Retrieves the Public IP address of the instance from checkip.amazonaws.com
Adds the IP address to the bastion Security Group

'''