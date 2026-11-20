# Publicar el portafolio en EC2

Abre `index.html` en tu navegador para revisar tu perfil y el enlace de contacto en LinkedIn antes de publicarlo.

## Subir el archivo

Estos pasos suponen que tu instancia EC2 ejecuta Linux, tiene acceso por SSH y ya cuenta con un servidor web. El ejemplo usa `/var/www/html`. Si tu servidor usa otra carpeta pública, ajusta esa ruta. Si ya hay un sitio en esa carpeta, usa una ruta o configuración separada para evitar reemplazarlo.

1. Desde tu computadora, en la carpeta donde guardaste `index.html`, copia el archivo a tu instancia. Sustituye la ruta de la llave, el usuario y la IP por los de tu instancia.
   ```sh
   scp -i /ruta/llave.pem index.html USUARIO@IP_PUBLICA:~/index.html
   ssh -i /ruta/llave.pem USUARIO@IP_PUBLICA
   ```
2. En la instancia, instala el archivo en la carpeta pública del sitio.
   ```sh
   sudo install -m 0644 ~/index.html /var/www/html/index.html
   ```
3. En el grupo de seguridad de EC2, permite el puerto de tu servidor web. Para HTTP es TCP 80. Para HTTPS es TCP 443 y el servidor también debe tener TLS configurado. Limita el acceso SSH a tu IP. [Reglas de grupos de seguridad de AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html#sg-rules-web-server)
4. Abre la dirección pública de la instancia en tu navegador y prueba la navegación y los enlaces de contacto antes de compartirla con reclutadores.

El único archivo que debes alojar para esta versión es `index.html`. El estilo ya está incluido.

Las imágenes de AWS y Certiprof se cargan desde Credly. Los nombres y las fechas de las certificaciones están incluidos en el HTML.
