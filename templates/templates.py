##### Utility Templates #####

ERROR_MESSAGE = '''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''

CONFIRM_MESSAGE = '''
* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    {}
* * * * * * * * * * * * * * * * * * * * * * * * * * * * *'''

PASSWORD_VAL_ERROR = '''
Please ensure your password has the following:
            - A minimum 6 characters
            - At least 1 capital letter
            - At least 1 number
'''

CONFIRM_DELETE = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
*       Are you sure you wish to delete the above?      *
*                                                       *
                   1. To delete        
*                                                       *
*           or enter any other key To cancel            *
* * *                                               * * *
                    OPTION: '''

REFINE_SEARCH = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
*      Is what you're looking for above? If so          *
*     Please enter the corresponding 'Ref Number'.      *
*                        Or                             *
*                 0. Return to menu                     *
* * *                                               * * *
                    OPTION: '''

##### Menu Templates #####

WELCOME_MENU = '''
* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                 Welcome to ebookstore!!!        

        Please select the corresponding number

            1. Login            2. Register
* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                    OPTION: '''

ADMIN_MENU = '''
* * *                                               * * * 
*   Please choose from the options below by entering    *
*               the corresponding number:               *

        1. Enter book           2. Update book
*       3. Delete book          4. Search books         *    
*       5. Admin management     0. Logout               *
* * *                                               * * *
                    OPTION: '''

ADMIN_MANAGE_MENU = '''
* * *              ADMIN MANAGEMENT                 * * * 
*   Please search for a account by one of the below     *
*    categories by entering the corresponding number    *

        1. Search account       2. Create admin
        3. Delete account       4. Update account           
*                                                       *
*         or enter any key to return to main menu       *
* * *                                               * * *
                    OPTION: '''

CUSTOMER_MENU = '''
* * *                                               * * * 
*   Please choose from the options below by entering    *
*               the corresponding number:               *

*       1. Search book          2. View basket          *
*       3. Manage account       0. Logout               *
* * *                                               * * *
                    OPTION: '''

##### Account Templates #####

ACCOUNT_SEARCH = '''
* * *               ACCOUNT SEARCH                  * * * 
*   Please search for a account by one of the below     *
*    categories by entering the corresponding number    *

        1. By id                2. By username
        3. By account type      4. view all                 
*                                                       *
*        or enter any key to return to main menu        *
* * *                                               * * *
                    OPTION: '''

ENUMERATED_ACCOUNT = '''
---------------------------------------------------------                                     
                                         Ref Number: {}
    Account ID:   {}
    Username:    '{}'
    Account Type: {}
    Address:      {}
---------------------------------------------------------'''

CUSTOMER_ADD = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
      Do you wish to add the above to you basket?       

*               1. Yes please                           *
*               Any Key: Return to Menu                 *       
* * *                                               * * *
                    OPTION: '''

ACC_HEADING = '''* * * * * * * * *    ACCOUNT PROFILE      * * * * * * * *'''

ACC_PROFILE = '''
---------------------------------------------------------
    Username:   {}
    Password:   {}
    Acc Type:   {}
    Address:    {}
'''

ACC_UPDATE = '''
* * *                                               * * *
*            What would you like to update?             *
*                                                       *
        ID        - {}                         
        Username  - {}
    1.  Password  - {}
    2.  Address   - {}
        Type      - {}
*                                                       *
*       or enter any key to return to main menu         *
* * *                                               * * *
                    OPTION: '''

SEARCH_ACC_OPTION = '''
* * *                                               * * *
*       Search for an account by selecting the          *
*               corresponding number:                   *

            1. By id        2. By username              
            3. By type         
*                                                       *
*         or enter any key to return to menu            *
* * *                                               * * *
                       OPTION: '''

SEARCH_ACC_TYPE = '''
* * *                                               * * *
*       Search for an account type by selecting         *
*            the corresponding number:                  *
*                                                       *
*           1. Admin        2. Customer                 *
* * *                                               * * *
                       OPTION: '''

ADD_ADMIN_ACCOUNT = '''
* * *                                               * * *
* To add an admin please answer the following questions *
* * *                                               * * *'''

CONFIRM_ACC_UPDATE = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
*             Are you happy with the above?             *
*                                                       *
*              1. Confirm      2. Restart               *
* * *                                               * * *
                        OPTION: '''

LOGOUT = '''
* * * * * * * * * * * * * * * * * * * * * * * * * * * * *

        {}, you have successfully
                logged out, Good Bye!!!

* * * * * * * * * * * * * * * * * * * * * * * * * * * * *'''

##### Book Templates #####

BOOK = '''
---------------------------------------------------------                                     
    ID:         {}
    Title:     '{}'
    Author:    '{}'
    Quantity:   {}
    Price p/u:  R{}
---------------------------------------------------------'''
ENUMERATED_BOOK = '''
---------------------------------------------------------                                     
                                         Ref Number: {}
    ID:         {}
    Title:     '{}'
    Author:    '{}'
    Quantity:   {}
    Price p/u:  R{}
---------------------------------------------------------'''
ENUMERATED_AUTHOR = '''
---------------------------------------------------------                                     
                                        Ref Number: {}
    Author:   {}
---------------------------------------------------------'''

CONFIRM_ADD_BOOK = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
*        If you are happy with the above, press         *
*                                                       *     
         1. To save         2. To start again 
*                                                       *
*        or enter any key to return to main menu        *
* * *                                               * * *
                    OPTION: '''

SEARCH_BOOK = '''
* * *                                               * * *
*     Please choose one of the categories below:        *
*                                                       *                                                    
            1. By id         2. By Title
            3. By Author     4. View all                              
*                                                       *
*           Any Key: To return to Main menu             *                
* * *                                               * * *
                    OPTION: '''

SEARCH_OPTION = '''
* * *                                               * * *
*       What would you like to do with this book?       *
*                                                       *
                1. Update Entry  
                2. Delete Entry            
*                                                       *
*      or enter any key to return to search again       *
* * *                                               * * *
                    OPTION: '''

UPDATE_BOOK = '''
* * *                                               * * *
*            What would you like to update?             *
*                                                       *
                    Book id: {}                         
    1. Title     - '{}'
    2. Author    - '{}'
    3. Quantity  -  {}
    4. Price p/u -  R{}
*                                                       *
*       or enter any key to return to main menu         *
* * *                                               * * *
                    OPTION: '''

REFINE_AUTHOR = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
*        Please choose from the above authors           *
*     by entering the corresponding 'Ref Number'        *
* * *                                               * * *
                    OPTION: '''

ADD_BOOK = '''
* * *                                               * * *
*  To add a book please answer the following questions  *
* * *                                               * * *'''

CONFIRM_UPDATE = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
*        If you are happy with the above, press         *
*                                                       *     
         1. To save             2. To start again 
         3. To update others
*                                                       *
*        or enter any key to return to main menu        *
* * *                                               * * *
                    OPTION: '''

##### Basket Templates #####


CUSTOMER_BASKET_HEADING = '''* * * * * * * * * * * *  BASKET!  * * * * * * * * * * * *'''

CUSTOMER_BASKET_EMPTY = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
                Total basket value: R0

*  'You currently don't have any books in your basket,  *
*         press any key to return to Main Menu          * 
* * *                                               * * *'''

CUSTOMER_BASKET_OPTION = '''      
      Please enter a corresponding 'Ref Number' to
              amend a book in your basket

*            {}. To continue to checkout               * 
*            Any Key: Return to Main Menu               *
* * *                                               * * *
                    OPTION: '''

CONFIRM_PURCHASE = '''
            Do you wish to purchase the above?          
*                                                       *
*           1. Yes           Any Key: No                *
* * *                                               * * *
                    OPTION: '''
UPDATE_BASKET = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
*           1. Update the quantity amount               *
*           2. Remove book from basket                  *
*           Any Key: Return to Main Menu                *
* * *                                               * * *
                    OPTION: '''

CUSTOMER_BASKET_VALUE = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
                Total basket value: R{}     
'''