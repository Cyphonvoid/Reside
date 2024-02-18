


#Bot detection solution

1) Create an account in the website that bot runs and have the bot login eeverytime it launches the new chrome window
2) Use UC driver /seleniumbase
3) Load cookies
4) User agent
5) change browser environment variables



_____________ 'Context Chaining' based list _________________

'-' means the sub part of some part

#NOTE
    - need to create a server based scrapper service
        - service can have multiple bots running
        - there will be a common session that bots can use
        - session has to be launched when server launches
            - session will contain necessary browser environment settings
                - session also contains the login info of websites

    - search scrapper bot will have a success score
        - this score will be used to determine searching effeciency
        - this score will determine which bots to launch next time upong failure
    
    - Need to create Python/Java API endpoints
        - endpoint will communicate over secure HTTP
    
    - how the service will work
        - service is hosted on some local machine 

        - webserver is launched
            - webserver launches session instance
                - session instance configures browser environment
            
            - webserver accepts routes GET, PUT, POST
                - GET :
                    - selects the route which contains BOT launcher:
                        - BOT launcher selects a bot to launch from success rating:
                            - bot is launched and scrapes data:
                                data is sent to the invoking function
                    
                    - Invoking function:
                        -data is jsonified and sent to whichever client requested:
                            - data contains the content the webserver address and as well the Bot ID:
                                - BOT ID also contains the BOT statistics like success rating etc.

                    - allows client to show available bots and websites

                - POST:
                    - may contain several configuration or setting based requests
                    - may allow client to select a particular bot
                    

        - BOT Folder:
            - contains launch file
            - contains other bot files for the specific website
            - contains json bot report file:
                - contains efficiency score of the bot
                - contains the inefficiency score as well
                - may contain error logs

            - contains json website environment file:
                - contains any login info
                - has website environment settings
                - any other website related stuff


        - BOT Functioning
            - static processing:
                - statically searches for elements
                - can not adapt to changing website
                - may need more code

            - dynamic processing:
                - adaptibility
                - May USE A.I Tech (Zeta A.I)
            

