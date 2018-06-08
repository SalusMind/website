# SalusMind

SalusMind is a service offered to organizations and schools to prevent tragedies.


## Database

### Organizations
* id
* name
* type
* description
* address
    * address-1
    * address-2
    * city
    * zipcode
* phone


### Users
* id
* username
* password
* name
* email
* affiliations
    * id
    * type
    * secret
* social
    * twitter
        * username
    * facebook
        * id
    * reddit
        * id
* profile
    * threat-level
    * tags
        * name
        * type
