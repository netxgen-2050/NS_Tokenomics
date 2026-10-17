---
title: Guía — cómo usar este repo con tu IA (Claude, ChatGPT, Gemini…)
created: 2026-10-17
audience: todo el equipo de NetX Gen
---

# Cómo usar este repo con tu IA

## 🌱 En un respiro

Este repo es la memoria del diseño de capital, tokenomics y estructura legal de Lighthouse. Lo podés cargar en tu IA y hacerle preguntas desde tu rol. **Trabajamos en la rama `legal-lab`**, que tiene el diseño nuevo. La forma más fácil: subí **un solo archivo** (el "paquete de contexto") a un proyecto de ChatGPT, Claude o Gemini, pegá las instrucciones de abajo y empezá a preguntar.

## 1. Acceso

- El repo es **privado**: `github.com/netxgen-2050/NS_Tokenomics`. Si no lo ves, pedile acceso a Gus.
- Usá siempre la rama **`legal-lab`** (no `main`): https://github.com/netxgen-2050/NS_Tokenomics/tree/legal-lab

## 2. Tres formas de cargarlo

### A. La más fácil: un archivo (ChatGPT, Claude, Gemini)

1. Descargá el paquete de contexto: https://github.com/netxgen-2050/NS_Tokenomics/blob/legal-lab/context-pack/NS_Tokenomics%20-%20full%20context.md (botón de descarga ⬇ arriba a la derecha del archivo).
2. Creá un proyecto:
   - **ChatGPT:** barra lateral → *Proyectos* → *Nuevo proyecto* → *Agregar archivos*.
   - **Claude (claude.ai):** *Projects* → *Create project* → *Add content* → subir el archivo.
   - **Gemini:** *Gems* → *Nuevo Gem* → *Conocimiento* → subir el archivo.
3. Pegá las **instrucciones del proyecto** (§3) en el campo de instrucciones.
4. Preguntá con los prompts de tu rol (§4).

El paquete es una foto del repo: cuando Gus avise que hay cambios, volvé a descargarlo y reemplazalo.

### B. Con un agente de código (Claude Code, Codex, Cursor)

```
git clone https://github.com/netxgen-2050/NS_Tokenomics.git
cd NS_Tokenomics
git checkout legal-lab
```

Claude Code lee `CLAUDE.md` y Codex lee `AGENTS.md` solos: ya saben las reglas del repo. Para regenerar el paquete de contexto: `python3 scripts/build_context_pack.py`.

### C. Para leer (Obsidian)

Abrí la carpeta clonada como vault de Obsidian. Los `[[enlaces]]` y los diagramas funcionan.

## 3. Instrucciones del proyecto (copiar y pegar)

```
Sos un asistente del equipo de NetX Gen para el proyecto Lighthouse (~1.000 ha, Mainqué, Río Negro, Argentina). El archivo adjunto es el repo NS_Tokenomics (rama legal-lab). Reglas:
1. Seguí las instrucciones de AGENTS.md (el primer archivo del paquete).
2. El diseño legal ACTUAL es el diseño B (docs 22 a 29): una fundación argentina es dueña de la tierra para siempre; un programa de fideicomisos por series financia proyectos productivos y regenerativos sobre derechos de superficie, con rendimiento con tope; una ONG independiente tiene servidumbres ecológicas perpetuas. Los docs 01 a 21 son trabajo anterior: usalos como contexto, no como la propuesta vigente.
3. Citá siempre el documento y la sección de donde sacás algo (por ejemplo "doc 25 §4"). Si algo no está en el repo, decilo; no lo inventes.
4. Separá lo que dice la ley de lo que es una decisión nuestra, y marcá lo legal como "a verificar con abogado". Nada de esto es asesoramiento legal, impositivo ni de inversión.
5. Los números son modelos ilustrativos ("qué tiene que ser cierto"), no pronósticos ni ofertas.
6. Respondé en español, simple y concreto. Si mi pregunta abre una decisión o una pregunta nueva, proponé cómo anotarla en el doc 07 (backlog).
```

## 4. Prompts para arrancar, por rol

**Vagner (CFO, modelo financiero)**
- "Resumime la cascada de pagos de una serie (doc 28 §1) y decime qué parámetros del doc 28 §7 necesito para mi modelo y cuáles faltan."
- "El doc 29 §5 dice que el capital de primera pérdida no se recupera en el 60% de los escenarios. Proponé dos estructuras de cascada alternativas y qué cambia para cada clase de inversor."
- "¿Cómo gana dinero NetX en el diseño B (doc 25 §1, doc 07 H-14)? Armame la lista de ingresos para el modelo de la holding."

**Franz (relación con BioPueblo e inversores)**
- "Explicame en lenguaje de dueño de tierra las cuatro formas de pagarle la tierra a BioPueblo (doc 25 §4). ¿Cuál defenderías primero y por qué?"
- "Escribime un pitch de 1 minuto para un inversor de impacto usando el recorrido 'USD 1.000 en el vino' (doc 28 §5), sin prometer rendimientos."
- "¿Qué le respondo a un inversor extranjero que pregunta si la Ley de Tierras le impide invertir (doc 25 §5, doc 21 §5b)?"

**Martín (masterplan)**
- "¿Qué zonas del 7A necesita cada motor de rendimiento (doc 23) y cuáles no necesitan loteo municipal?"
- "¿Qué implica para el masterplan que la tierra se dé por derechos de superficie por zona en vez de lotes (doc 25 §1)?"
- "¿Qué datos de vivienda faltan para el recorrido 'vivir acá en 10 años' (doc 28 §4 y §7)?"

**Juanpi (plataformas de tokenización)**
- "¿Qué instrumentos del diseño B se tokenizarían, cuándo y sobre qué rieles (doc 28 §3, doc 26)?"
- "¿Qué necesita la Serie Madre para ser tokenizable en el régimen de la CNV? Hacé una lista de requisitos y de preguntas para el abogado."
- "¿Cómo evitamos una corrida sobre la Serie Madre tokenizada (doc 29, peligro K2)?"

**Abogado/a (cuando se sume)**
- "Leé el doc 27 y decime qué preguntas son más urgentes para poder capitalizarnos en los próximos 3 meses."
- "¿Dónde ves riesgos en la figura de la fundación como dueña de la tierra (doc 25 §1 y §8)?"

**Cualquiera**
- "Explicame el diseño B como si no supiera nada de leyes ni de tokens, con un ejemplo."
- "¿Qué está decidido, qué está propuesto y qué está abierto? (doc 07 §I)"

## 5. Reglas del equipo

- **No subas nada de `private/`** (no está en GitHub, y no debe salir de la máquina de Gus).
- **Lo que diga la IA es un borrador**, no un dictamen. Lo legal lo decide un abogado; los números, el modelo de Vagner.
- **Para devolver lo que aprendiste:**
  - **Si es corto:** mandáselo a Gus.
  - **Si es un cambio:** creá una rama desde `legal-lab` con tu nombre (`cambios_franz`, `cambios_vagner`…) y abrí un pull request **hacia `legal-lab`**.
