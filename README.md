# oraclePyLambda

This example demostrates how to build a Lambda (Python) that connects to an RDS Oracle instance


## Introduction

This example demostrates how to use build a Lambda (Python) function that can connect to RDS Oracle Instance. 

## Step 0 - Create the RDS Oracle DB

## Step 1 - Configure the DB
The connection to the database is encrypted via SSL. Download the PEM certificate required [here] (http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)
Create a user on your RDS instance with username/password.

## Step 2 - Create Lambda function and setup Env variables
The code depends on a few environment variables that need to match your deployed RDS instance:

```
endpoint: somename.someuniquevalue.us-west-2.rds.amazonaws.com
```
```
password: somepassword
```
```
my_db: DB name
```
```
user: Rds username
```

VPC enable your Lambda function and attach it to the same subnet your RDS instance is in.

## Step 3 - Include Oracle dependencies

Required Dependencies:
	• Python cx_Oracle module (http://cx-oracle.readthedocs.io/en/latest/installation.html)
	• Oracle Instant Client (https://oracle.github.io/odpi/doc/installation.html#linux)
	• Libaio libraries

Download the Linux installations for all dependencies, and use all 32bit or all 64bit.
Place all dependencies in the /lib directory

Install the cx_Oracle client:
```
python3  -m pip install cx_Oracle -t .
```
```
python  -m pip install cx_Oracle -t .
```

## Resources

- **oracleTest.py** - Python Based Lambda function that connects to RDS Oracle and performs a simple SELECT statement
