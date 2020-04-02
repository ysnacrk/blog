# Blog

This repository includes my blog.

The motivation doing this project is understand how a small backend project works and learn how to deploy a project on Linux server.

Here is my [blog](http://yasinacierik.xyz)

Empty for now but hopefully nice articles will come in the future

# Installation

Clone repo and run 

`. install.sh`

# Configuration

Open flask conf.json file and set variables

                            |
--------------------------  | -----------------------------------------------------------------------
 **SECRET_KEY**             | Secret key that will be used for securely signing the session cookie   
 **SQLALCHEMY_DATABASE_URI**|  Where the database file will be stored                                
 **RECAPTCHA_PRIVATE_KEY**  | You need google recaptcha keys for secure login                        
 **RECAPTCHA_PUBLIC_KEY**   |  You need google recaptcha keys for secure login                       

Markdown | Less | Pretty
--- | --- 
*Still* | `renders` | **nicely**
1 | 2 | 3

Create database tables and user

`python3 setup.py <username> <password>`


# Run

`python3 run.py`




# Documentation

The construction and deploy stages of the blog
