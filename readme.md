
# howto start - local changes

docker-compose has been adapted for our local test with Elasticsearch and apm-server already running. 

The ```docker-compose.yml``` uses some variables. Use some start script like this:
```
#!/bin/bash

export APM_PASSWORD=[PW_HERE]
export ELASTIC_SERVER=[ELASTIC_SERVER]
export APM_SERVER_NAME=[APM_SERVER]

cd [DIR_WITH_FILES]

docker-compose up
```


# Spring PetClinic Application with the Elastic Stack (spring-framework-petclinic extend )

This version of the Spring Petclinic application utilises the [REST API implementation](https://github.com/spring-petclinic/spring-petclinic-rest) as its core.

The [reactjs version](https://github.com/spring-petclinic/spring-petclinic-reactjs) has been integrated and updated to use this REST interface and the latest version of React.

A docker compose allows the user to run the application, backed with Mysql as the data layer, with Elastic APM and Beat instrumentation enabled. The following services are deployed:

- Pet Clinic via embedded Tomcat with REST API. Instrument with Elastic Java Agent.
- React UI for Pet Clinic using above. Instrument with Elastic RUM Agent.
- Elasticsearch
- Kibana
- MySQL
- Packetbeat - **PENDING**
- Metricbeat - **PENDING**
- Filebeat - **PENDING**
- Nginx - **PENDING**

This allows collection of the following metrics:

- Java APM data as available from the Java Agent i.e. transactions, spans and errors
- MYSQL, HTTP traffic via Packetbeat **PENDING**
- Application Logs + NGINX Logs via Filebeat **PENDING**
- JMX, Docker, Mysql, Nginx metrics via Metricbeat  **PENDING**



## Running Petclinic with the Elastic Stack


`ES_VERSION=6.4.2 docker-compose -f docker-compose.yml up`

Other versions of the Elasticstack may work. Currently, only version 6.4.2 has been tested.

## Running petclinic locally for development
```
	git clone https://github.com/spring-petclinic/spring-petclinic-rest.git
	cd spring-petclinic-rest
	./mvnw spring-boot:run
```

You can then access petclinic here: http://localhost:9966/petclinic/


## Understanding the Spring Petclinic application with a few diagrams
<a href="https://speakerdeck.com/michaelisvy/spring-petclinic-sample-application">See the presentation here</a>


## Swagger REST API documentation presented here (after application start):
<a href="http://localhost:9966/petclinic/swagger-ui.html">http://localhost:9966/petclinic/swagger-ui.html</a>


## Development - Database configuration

In its default configuration, Petclinic uses an in-memory database (HSQLDB) which
gets populated at startup with data.
A similar setups is provided for MySql and PostgreSQL in case a persistent database configuration is needed.
To run petclinic locally using persistent database, it is needed to change profile defined in application.properties file.

For MySQL database, it is needed to change param "hsqldb" to "mysql" in string
```
spring.profiles.active=hsqldb,spring-data-jpa
```
 defined in application.properties file.

Before do this, would be good to check properties defined in application-mysql.properties file.

```
spring.datasource.url = jdbc:mysql://localhost:3306/petclinic?useUnicode=true
spring.datasource.username=pc
spring.datasource.password=petclinic 
spring.datasource.driver-class-name=com.mysql.jdbc.Driver 
spring.jpa.database=MYSQL
spring.jpa.database-platform=org.hibernate.dialect.MySQLDialect
spring.jpa.hibernate.ddl-auto=none
```      

You may also start a MySql database with docker:

```
docker run --name mysql-petclinic -e MYSQL_ROOT_PASSWORD=petclinic -e MYSQL_DATABASE=petclinic -p 3306:3306 mysql:5.7.8
```

or use the docker-compose-mysql.yml` file provided.

For PostgeSQL database, it is needed to change param "hsqldb" to "postgresql" in string
```
spring.profiles.active=hsqldb,spring-data-jpa
```
 defined in application.properties file.

Before do this, would be good to check properties defined in application-postgresql.properties file.

```
spring.datasource.url=jdbc:postgresql://localhost:5432/petclinic
spring.datasource.username=postgres
spring.datasource.password=petclinic
spring.datasource.driver-class-name=org.postgresql.Driver
spring.jpa.database=POSTGRESQL
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=none
```
You may also start a Postgres database with docker:

```
docker run --name postgres-petclinic -e POSTGRES_PASSWORD=petclinic -e POSTGRES_DB=petclinic -p 5432:5432 -d postgres:9.6.0
```

## Security configuration
In its default configuration, Petclinic doesn't have authentication and authorization enabled.

### Basic Authentication
In order to use the basic authentication functionality, turn in on from the application.properties file
```
basic.authentication.enabled=true
```
This will secure all APIs and in order to access them, basic authentication is required.
Apart from authentication, APIs also require authorization. This is done via roles that a user can have.
The existing roles are listed below with the corresponding permissions 
* OWNER_ADMIN -> OwnerController, PetController, PetTypeController (getAllPetTypes and getPetType), VisitController
* VET_ADMIN   -> PetTypeController, SpecialityController, VetController
* ADMIN       -> UserController

There is an existing user with the username admin and password admin that has access to all APIs.
 In order to add a new user, please use the following API:
```
POST /api/users
{
    "username": "secondAdmin",
    "password": "password",
    "enabled": true,
    "roles": [
    	{ "name" : "OWNER_ADMIN" }
	]
}
```

## Working with Petclinic in Eclipse/STS

### prerequisites
The following items should be installed in your system:
* Maven 3 (http://www.sonatype.com/books/mvnref-book/reference/installation.html)
* git command line tool (https://help.github.com/articles/set-up-git)
* Eclipse with the m2e plugin (m2e is installed by default when using the STS (http://www.springsource.org/sts) distribution of Eclipse)

Note: when m2e is available, there is an m2 icon in Help -> About dialog.
If m2e is not there, just follow the install process here: http://eclipse.org/m2e/download/


### Steps:

1) In the command line
```
git clone https://github.com/spring-petclinic/spring-petclinic-rest.git
```
2) Inside Eclipse
```
File -> Import -> Maven -> Existing Maven project
```


