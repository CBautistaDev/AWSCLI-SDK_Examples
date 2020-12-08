# Command	Purpose
Make a bucket	
## aws s3 mb s3://my-bucket
List all buckets	
## aws s3 ls
List the contents of a specific bucket	
## aws s3 ls s3://my-bucket
Upload a file to a bucket	
## aws s3 cp file s3://my-bucket/file
Download a file from a bucket	
## aws s3 cp s3://my-bucket/file file
Copy a file between buckets	
## aws s3 cp s3://bucket1/file s3://bucket2/file
Synchronize a directory with an S3 bucket	
## aws s3 sync my-directory s3://my-bucket/
