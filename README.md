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

## Resources

- **oracleTest.py** - Python Based Lambda function that connects to RDS Oracle and performs a simple SELECT statement
