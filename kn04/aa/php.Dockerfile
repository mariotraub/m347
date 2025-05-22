FROM php:8.0-apache

COPY ./db.php /var/www/html/
COPY ./info.php /var/www/html/

RUN docker-php-ext-install mysqli

EXPOSE 80

