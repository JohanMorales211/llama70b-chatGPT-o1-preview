import streamlit as st
import groq
import os
import json
import time
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la API key desde la variable de entorno
api_key = os.getenv("GROQ_API_KEY")

# Pasar la API key al cliente de Groq
client = groq.Groq(api_key=api_key)

def make_api_call(messages, max_tokens, is_final_answer=False):
    """
    Realiza una llamada a la API de Groq para generar una respuesta.
    Maneja errores y reintenta hasta 3 veces.
    """
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.2,
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            if attempt == 2:
                if is_final_answer:
                    return {"title": "Error", "content": f"Falló la generación de la respuesta final después de 3 intentos. Error: {str(e)}"}
                else:
                    return {"title": "Error", "content": f"Falló la generación del paso después de 3 intentos. Error: {str(e)}", "next_action": "final_answer"}
            time.sleep(1)  # Esperar 1 segundo antes de volver a intentar

def generate_response(prompt):
    """
    Genera una respuesta paso a paso utilizando el modelo de lenguaje.
    """
    messages = [
        {"role": "system", "content": """Eres un asistente de IA experto que explica tu razonamiento paso a paso. Para cada paso, proporciona un título que describa lo que estás haciendo en ese paso, junto con el contenido. Decide si necesitas otro paso o si estás listo para dar la respuesta final. Responde en formato JSON con las claves 'title', 'content' y 'next_action' (ya sea 'continue' o 'final_answer'). USA TANTOS PASOS DE RAZONAMIENTO COMO SEA POSIBLE. AL MENOS 3. TEN EN CUENTA TUS LIMITACIONES COMO LLM Y LO QUE PUEDES Y NO PUEDES HACER. EN TU RAZONAMIENTO, INCLUYE LA EXPLORACIÓN DE RESPUESTAS ALTERNATIVAS. CONSIDERA QUE PUEDES ESTAR EQUIVOCADO, Y SI ESTÁS EQUIVOCADO EN TU RAZONAMIENTO, DÓNDE ESTARÍA. PRUEBA COMPLETAMENTE TODAS LAS OTRAS POSIBILIDADES. PUEDES ESTAR EQUIVOCADO. CUANDO DIGAS QUE ESTÁS REEXAMINANDO, REEXAMINA REALMENTE Y USA OTRO ENFOQUE PARA HACERLO. NO TE LIMITES A DECIR QUE ESTÁS REEXAMINANDO. USA AL MENOS 3 MÉTODOS PARA DERIVAR LA RESPUESTA. USA LAS MEJORES PRÁCTICAS.

Ejemplo de una respuesta JSON válida:
```json
{
    "title": "Identificar información clave",
    "content": "Para comenzar a resolver este problema, necesitamos examinar cuidadosamente la información proporcionada e identificar los elementos cruciales que guiarán nuestro proceso de solución. Esto implica...",
    "next_action": "continue"
}```
"""},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": "¡Gracias! Ahora pensaré paso a paso siguiendo mis instrucciones, comenzando al principio después de descomponer el problema."}
    ]
    
    steps = []
    step_count = 1
    total_thinking_time = 0
    
    while True:
        start_time = time.time()
        step_data = make_api_call(messages, 300)
        end_time = time.time()
        thinking_time = end_time - start_time
        total_thinking_time += thinking_time
        
        steps.append((f"Paso {step_count}: {step_data['title']}", step_data['content'], thinking_time))
        
        messages.append({"role": "assistant", "content": json.dumps(step_data)})
        
        if step_data['next_action'] == 'final_answer' or step_count > 25: # Máximo de 25 pasos para evitar tiempo de pensamiento infinito. Se puede ajustar.
            break
        
        step_count += 1

        # Rendimiento después de cada paso para que Streamlit se actualice
        yield steps, None  # No estamos generando el tiempo total hasta el final

    # Generar respuesta final
    messages.append({"role": "user", "content": "Por favor, proporciona la respuesta final basada en tu razonamiento anterior."})
    
    start_time = time.time()
    final_data = make_api_call(messages, 200, is_final_answer=True)
    end_time = time.time()
    thinking_time = end_time - start_time
    total_thinking_time += thinking_time
    
    steps.append(("Respuesta final", final_data['content'], thinking_time))

    yield steps, total_thinking_time

def main():
    """
    Función principal de la aplicación Streamlit.
    """
    st.set_page_config(page_title="Llama-3.1 70B", page_icon="🧠", layout="wide")
    
    st.title("Llama-3.1 70B razonando como ChatGPT-o1-preview")
    st.markdown("<p style='text-align: center; background-color: white; color: black;'>Creado por Johan Morales</p>", unsafe_allow_html=True)

    st.markdown("""
    Este prototipo utiliza indicaciones especiales para guiar a Llama-3.1 a través de un proceso de razonamiento más transparente. 
    Explora diferentes enfoques y evalúa sus propias limitaciones para llegar a una respuesta. 
    Ten en cuenta que se trata de una tecnología en desarrollo y la precisión puede variar.
    """)
    
    # Entrada de texto para la consulta del usuario
    user_query = st.text_input("Introduce tu consulta:", placeholder="p. ej., ¿Cuántas 'R' hay en la palabra fresa?")
    
    if user_query:
        st.write("Generando respuesta...")
        
        # Crear elementos vacíos para contener el texto generado y el tiempo total
        response_container = st.empty()
        time_container = st.empty()
        
        # Generar y mostrar la respuesta
        for steps, total_thinking_time in generate_response(user_query):
            with response_container.container():
                for i, (title, content, thinking_time) in enumerate(steps):
                    if title.startswith("Respuesta final"):
                        st.markdown(f"### {title}")
                        st.markdown(content.replace('\n', '<br>'), unsafe_allow_html=True)
                    else:
                        with st.expander(title, expanded=True):
                            st.markdown(content.replace('\n', '<br>'), unsafe_allow_html=True)
            
            # Solo mostrar el tiempo total cuando esté disponible al final
            if total_thinking_time is not None:
                time_container.markdown(f"**Tiempo total de pensamiento: {total_thinking_time:.2f} segundos**")

if __name__ == "__main__":
    main() 