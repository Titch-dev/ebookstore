## Overview
A book store application, enabling CRUD operations for administrators and customers. 

## Features
### Administrators:
- Add new books to the database
- Update book information
- Delete books from the database
- Search the database to find a specific book
    - by id
    - by title
    - by author
    - return all


- Add new administrator accounts
- Update account profile
- Delete account users
- Search the database to find a specific account
  - by id
  - by username
  - by account type ('admin', 'customers')
### Customers:
- Update account profile
- Search database to return customer basket
- Purchase books from customer basket (requires customer address)
- Search the database for books to add to customer basket
  - by id
  - by title
  - by author
  - return all

## Installation
### Set up the database:
1. In project root, open file *data/db_build.py*
   1. Uncomment the preferred database and save file
2. Run file *data/db_build.py*

### Set up the environment:
1. Open file *env/database_context.py*
   1. Uncomment the preferred database to connect the app to

## Usage
Login into the application with default users:
- username: **admin1**
- password: **Pa$$word1**


- username: **customer1**
- password: **Pa$$word1**


