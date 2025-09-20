# Juego del Tiro Parabólico
Un juego bastante sencillo de destreza programado en la interface visual de Python. El código original fie obtenido del sitio Grant Jenks, pero por preferencias personales, en este repositorio le hicimos algunos cambios a las características del juego.
## Acerca del Código Base y su Funcionamiento
La dinámica es bastante simple, en la pantalla aparecen círculos de color azul que son los objetivos, estos se tiene que eliminar con un proyectil, color rojo, que obtiene su velocidad de tiro por la posición del clic dado en pantalla. Mientras más alto el clic, más rápido el proyectil, pero si uno de los objetivos alcanza el borde contrario de donde se generan, el juego se detiene.
## Cambios Realizados al Código Base
Para volver la experiencia más entretenida, generamos algunos cambios al código original en este repositorio.
### Primer Cambio: Velocidad
Volvimos tanto los proyectiles como a los objetivos un poco más rápidos para agilizar el juego.
### Segundo Cambio: Juego Interminable
En lugar que el juego se termine cuando un objetivo llega al borde, este se vuelve a generar del lado de inicio, por lo que el juego se vuelve un juego infinito, para poder terminarlo en cuanto uno quiera.
