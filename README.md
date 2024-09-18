# Llama-3.1 70B razonando como ChatGPT-o1-preview

**Explora el poder del prompting para guiar a Llama-3.1 70B a través de un proceso de razonamiento similar a ChatGPT-o1-preview, visualizando cada paso y fomentando la transparencia en la toma de decisiones del modelo.**

Este prototipo utiliza estrategias de prompting especiales para que Llama-3.1 70B aborde problemas lógicos de una manera más deliberada y transparente. El modelo evalúa sus propias limitaciones, explora múltiples enfoques y proporciona un registro visual de su proceso de razonamiento.

![Imagen de Llama generando código](https://venturebeat.com/wp-content/uploads/2024/01/nuneybits_Code_llama_be1422ea-d027-46ed-9491-c3b76df94971-transformed.webp)

**¡Descubre cómo las indicaciones cuidadosamente diseñadas pueden mejorar la capacidad de razonamiento de los modelos de lenguaje grandes!** 

## Características ✨

* **Razonamiento paso a paso:**  Observa cómo Llama-3.1 70B descompone un problema en pasos lógicos y los aborda uno por uno.
* **Prompting estratégico:**  Utiliza indicaciones que fomentan la autoevaluación, la exploración de alternativas y la transparencia en el proceso de razonamiento.
* **Visualización del proceso:**  Cada paso del razonamiento del modelo se muestra con su título y contenido, lo que facilita la comprensión de su "pensamiento".
* **Modelo de código abierto:**  Aprovecha la potencia de Llama-3.1 70B, un modelo de lenguaje grande de código abierto.

## Cómo Funciona 🔄

El prototipo utiliza una serie de indicaciones (prompts) diseñadas para guiar a Llama-3.1 70B a través de un proceso de razonamiento estructurado. Estas indicaciones incluyen:

* **Instrucciones para pensar paso a paso:** Se le pide al modelo que divida el problema en pasos lógicos y que proporcione un título y contenido para cada uno.
* **Conciencia de las limitaciones:** Se le recuerda al modelo sus propias limitaciones como LLM y se le anima a considerar dónde podría estar equivocado.
* **Exploración de alternativas:** Se le pide al modelo que explore múltiples enfoques para resolver el problema y que considere diferentes posibilidades.
* **Uso de mejores prácticas:** Se le indica al modelo que utilice las mejores prácticas en su razonamiento, lo que puede mejorar la calidad de sus respuestas.

## Ejemplos 💡

> **¡IMPORTANTE!** 
> Este es un prototipo y la precisión del razonamiento de Llama-3.1 70B puede variar.  

**Problema de la Fresa:**

Prompt: ¿Cuántas 'R' hay en la palabra fresa?

El modelo generará una serie de pasos de razonamiento, incluyendo la identificación de la palabra "fresa", la descomposición de la palabra en letras individuales y el conteo del número de 'R'.

**Otros ejemplos:**

Puedes probar con diferentes tipos de preguntas que requieran razonamiento lógico, como problemas matemáticos simples, acertijos o preguntas de comprensión de lectura.

## Instalación 🛠️

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/JohanMorales211/llama70b-chatGPT-o1-preview.git
   ```
2. **Navega al directorio del proyecto:**
   ```bash
   cd llama70b-chatGPT-o1-preview
   ```
3. **Crea un entorno virtual:**
   ```bash
   python3 -m venv venv
   ```
4. **Activa el entorno virtual:**
   ```bash
   source venv/bin/activate
   ```
5. **Instala las dependencias:**
   ```bash
   pip3 install -r requirements.txt
   ```
6. **Configura tu clave API de Groq:**
   Crea un archivo `.env` en la raíz del proyecto y agrega la siguiente línea, reemplazando `tu_clave_api` con tu clave API de Groq:
   ```
   GROQ_API_KEY=tu_clave_api
   ```
7. **Inicia la aplicación:**
   ```bash
   streamlit run app.py
   ```

## Uso 🚀

Una vez que la aplicación esté en ejecución, introduce tu consulta en el cuadro de texto y observa cómo Llama-3.1 70B razona paso a paso para llegar a una respuesta. 


## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si encuentras algún error o quieres agregar nuevas características, no dudes en abrir un issue o enviar un pull request.

---

<div align="center">
  <p>Creado con ❤️ por [Johan Morales]</p>
  <img src="https://media.giphy.com/media/hvRJCLFzcasr6/giphy.gif" width="200" alt="Animación de IA"> 
</div>

--- 
