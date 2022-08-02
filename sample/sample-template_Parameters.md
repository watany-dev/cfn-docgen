| Name                | Type                       | Description                                                                         | Default   |   MaxLength |   MinLength | MaxValue   | MinValue   | AllowedPattern                                       | AllowedValues                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | ConstraintDescription                             | NoEcho   | Filename             |
|:--------------------|:---------------------------|:------------------------------------------------------------------------------------|:----------|------------:|------------:|:-----------|:-----------|:-----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------|:---------|:---------------------|
| BastionKeyName      | AWS::EC2::KeyPair::KeyName | Name of an existing EC2 KeyPair to enable SSH access to the bastion host            |           |             |             |            |            |                                                      | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | must be the name of an existing EC2 KeyPair.      | False    | sample-template.json |
| KeyName             | AWS::EC2::KeyPair::KeyName | Name of an existing EC2 KeyPair to enable SSH access to the Elastic Beanstalk hosts |           |             |             |            |            |                                                      | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | must be the name of an existing EC2 KeyPair.      | False    | sample-template.json |
| SSHLocation         | String                     | Lockdown SSH access to the bastion host (default can be accessed from anywhere)     | 0.0.0.0/0 |          18 |           9 |            |            | (\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2}) | []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | must be a valid CIDR range of the form x.x.x.x/x. | False    | sample-template.json |
| BastionInstanceType | String                     | Bastion Host EC2 instance type                                                      | t2.small  |             |             |            |            |                                                      | ['t1.micro', 't2.nano', 't2.micro', 't2.small', 't2.medium', 't2.large', 'm1.small', 'm1.medium', 'm1.large', 'm1.xlarge', 'm2.xlarge', 'm2.2xlarge', 'm2.4xlarge', 'm3.medium', 'm3.large', 'm3.xlarge', 'm3.2xlarge', 'm4.large', 'm4.xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.10xlarge', 'c1.medium', 'c1.xlarge', 'c3.large', 'c3.xlarge', 'c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c4.large', 'c4.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'g2.2xlarge', 'g2.8xlarge', 'r3.large', 'r3.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'i2.xlarge', 'i2.2xlarge', 'i2.4xlarge', 'i2.8xlarge', 'd2.xlarge', 'd2.2xlarge', 'd2.4xlarge', 'd2.8xlarge', 'hi1.4xlarge', 'hs1.8xlarge', 'cr1.8xlarge', 'cc2.8xlarge', 'cg1.4xlarge'] | must be a valid EC2 instance type.                | False    | sample-template.json |
| NATInstanceType     | String                     | NAT Device EC2 instance type                                                        | t2.small  |             |             |            |            |                                                      | ['t1.micro', 't2.nano', 't2.micro', 't2.small', 't2.medium', 't2.large', 'm1.small', 'm1.medium', 'm1.large', 'm1.xlarge', 'm2.xlarge', 'm2.2xlarge', 'm2.4xlarge', 'm3.medium', 'm3.large', 'm3.xlarge', 'm3.2xlarge', 'm4.large', 'm4.xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.10xlarge', 'c1.medium', 'c1.xlarge', 'c3.large', 'c3.xlarge', 'c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c4.large', 'c4.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'g2.2xlarge', 'g2.8xlarge', 'r3.large', 'r3.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'i2.xlarge', 'i2.2xlarge', 'i2.4xlarge', 'i2.8xlarge', 'd2.xlarge', 'd2.2xlarge', 'd2.4xlarge', 'd2.8xlarge', 'hi1.4xlarge', 'hs1.8xlarge', 'cr1.8xlarge', 'cc2.8xlarge', 'cg1.4xlarge'] | must be a valid EC2 instance type.                | False    | sample-template.json |