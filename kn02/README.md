# Dockerfiles

```Dockerfile
FROM nginx  # Mit FROM kann man das Origin Image Definieren
COPY static-html-directory /var/www/html # Mit COPY kann man ein Verzeichnis oder eine Datei auf den gegebenen Pfad im Docker Container kopieren.
EXPOSE 	80	# Mit EXPOSE 80 wird gesagt das der port 80 offen ist und gemappt werden sollte.
```
