#select {nombre, correo ##lo que quieras} from usuarios (nombre de la tabla) con un asterisco entre sin las lavves despues del select se manda todo
## para mandar de uno en especifico select {} from (nombre de tabla) from (nombre de la tabla) where correo =" " and contraseña=""

### insert into __( ) values ("","","") 
### insert into usuarios values ("", "", "") para insertar en todas las filas
### insert into usuarios (nom, correo, contraseña) values ("", "", "") para insertar en algunas de las filas

# Update ___ set
# Update usuarios set contraseña == " " where id = 1 (por ejemplo)
# Update usuarios set contraseña == " ", correo==" ", nombre== " ", where id = 1 (por ejemplo)

#delete from ___ where id ___
#delate from usuarios where id = 1
#delate from usuarios ##eso hace que elimina todos los datos de la tabla

