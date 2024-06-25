# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Tratando de programar sin desprogramarte el cerebro </h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("IMG_9345.JPG", caption='ronald en el mar', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Hola, me llamo Ronald y tengo 20 años. Desde muy joven, he tenido una gran pasión por la fotografía, la música y el arte en general. Considero que un mundo sin arte sería un lugar muy aburrido y vacío, ya que el arte nos permite expresar nuestras emociones, contar historias y conectar con los demás de una manera única y profunda.

En mi tiempo libre, disfruto explorando diferentes formas de arte. La fotografía es una de mis actividades favoritas porque me permite capturar momentos especiales y ver el mundo desde diferentes perspectivas. Me encanta experimentar con la luz y las sombras, y buscar la belleza en lo cotidiano.

La música también es una gran parte de mi vida. Toco varios instrumentos y disfruto tanto escuchando como creando música. La música tiene el poder de transformar el estado de ánimo y de llevarnos a otros lugares, y me fascina cómo puede unir a las personas sin importar sus diferencias.

Además, soy un gran admirador de las artes visuales. Me gusta visitar museos y galerías, y siempre estoy en busca de nuevas exposiciones y artistas emergentes. Creo que el arte visual es una forma poderosa de comunicación que puede inspirar, provocar reflexión y generar cambios en la sociedad.

Recientemente, he decidido aprender a programar en Python. Aunque es un mundo completamente nuevo para mí, estoy muy entusiasmado con las posibilidades que ofrece. Veo la programación como otra forma de creatividad, una herramienta que puedo usar para construir y dar vida a mis ideas de maneras que antes no podía imaginar. Al igual que el arte, la programación requiere paciencia, práctica y una mente abierta para resolver problemas y superar desafíos.

Estoy seguro de que mi interés por la fotografía, la música y el arte me ayudará a encontrar enfoques únicos y creativos en el mundo de la programación. Estoy ansioso por ver cómo puedo combinar estas pasiones para crear proyectos innovadores y significativos.
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.


# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """  
Programar ha sido un trabajo complicado el cual he ido aprendiendo a lo largo del ciclo. Estoy comenzando a compreder Python y me parece muy interesante. Aunque al principio fue un poco desafiante entender algunos conceptos, cada día me siento más cómodo con el lenguaje. Me gusta cómo puedo usar Python para resolver problemas y crear programas útiles. Estoy emocionado por seguir aprendiendo y mejorar mis habilidades.


"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>quieres ver los gráficos? despliega aquí⬇</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['grafico pastel', 'Gráfico de barras 1', 'grafico de barras 2']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'grafico pastel':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>Se puede apreciar porcentajes de tantos goles como local y como visita </div>", unsafe_allow_html=True)
    sidebar.image("milan piechart.png", caption='grafico de pastel de la frecuencia de goles del Milan tanto como local y como visita', width=500)
    pass
elif grafico_seleccionado == 'Gráfico de barras 1':
    sidebar.markdown("<div style='text-align: justify'>Se puede apreciar la frecuencia de goles en una barra vertical</div>", unsafe_allow_html=True)
    sidebar.image("descarga.png", caption='promedio de tarjetas amarillas por equipo', width=500)
    pass
elif grafico_seleccionado == 'grafico de barras 2':
    sidebar.markdown("<div style='text-align: justify'> se puede apreciar la frecuencia de goles en una barra vertical</div>", unsafe_allow_html=True)
    sidebar.image("milan estadistica.png", caption='frecuencia de goles de Milan', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas':: Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
