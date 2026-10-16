---
title: Prompt de deep research legal — nivel de compliance y margen de maniobra lícito de la tokenomics RAIZ
created: 2026-10-13
updated: 2026-10-13 (v0.2, en español; incorpora la llamada del 12-10, el modelo híbrido y la Constitución)
status: es un prompt para correr, no un dictamen. Nada de esto es asesoramiento legal, fiscal ni de inversión.
owner: Gus (autor del encargo) → Gabriel (lo corre contra su bóveda)
audience: Gabriel y su asistente de IA; después Néstor / el estudio jurídico de NetX
---

# Prompt de deep research legal (para la bóveda de Gabriel)

Volver a [[00 - README]] · Mapa legal: [[06 - Legal Friction Map]] · Backlog: [[07 - Open Questions and Research Backlog]]

(Este archivo está en español, a diferencia del resto del repo, porque se envía aparte a Gabriel y al estudio jurídico.)

## 🌱 En una frase

Tenemos un diseño de tokens y capital (este repo) escrito por no abogados, y una arquitectura legal distinta que Franz generó con Gemini después de la llamada del 12-10-2026, sin el contexto del repo. Las dos chocan en puntos importantes, y además el equipo dejó abierta la pregunta de si vender o no algunos lotes. Este archivo es el encargo para el asistente de IA de Gabriel: leer todo, contrastarlo con la ley vigente hoy, decirnos **qué tan compliant es cada pieza** y encontrar **la versión más ágil y atractiva para el capital que siga siendo genuinamente lícita**. Tiene que decirnos tanto dónde nos pasamos de la raya como dónde somos más cautos de lo que la ley exige.

## Cómo correrlo (Gabriel)

1. Cloná o actualizá `https://github.com/netxgen-2050/NS_Tokenomics` y parate en tu rama. Hacé que el repo sea legible desde la sesión donde tu asistente trabaja sobre tu bóveda. Los documentos 16, 17 y 18 son nuevos (13-10-2026); si todavía no están en `main`, pedíselos a Gus.
2. Exportá el Google Doc de Franz (*"Arquitectura Legal, Financiera, Tokenómica y de Gobernanza para el Desarrollo Territorial Regenerativo: Barrio Lighthouse VRN (Biopueblo)"*, id `1zd8PbYirK6I0gG8EOikRdZHPxp1WymSmtDXX9YlUFAk`) a Markdown o PDF y dejalo en tu bóveda, por si el asistente no puede abrir Google Docs.
3. Si tu bóveda no tiene la investigación del 29-09-2026 (`Investigacion — DRS, fideicomisos y tokenizacion (Lighthouse VRN) 2026-09-29.md` y `requisitos-legales-plataforma-2026-09-29.md`), pedísela a Gus: es la base legal sobre la que se armó el repo.
4. Usá una sesión **con acceso web** y el modelo más capaz que tengas. Es una tarea larga (horas, varias pasadas).
5. Pasale al asistente todo lo que está debajo de la línea. Revisá vos el resultado antes de que vaya al estudio y abrí un pull request de tu rama a `main`.

---

## EL ENCARGO (pasarle al asistente todo desde acá)

### 1. Quién pregunta y para qué

Estás ayudando al equipo de **NetX Gen** a diseñar la parte legal de **Lighthouse**: unas 1.000 ha (Macrolote 7, zona de Mainqué, Río Negro, Argentina) dentro de las ~10.000 ha de BioPueblo, pensadas como un asentamiento regenerativo de 10–12 comunidades. Trabajás en la bóveda de **Gabriel**, COO, que lidera lo legal. El diseño lo hizo Gus (diseño de tokens y capital) con aportes de Vagner (CFO), Franz (relación con BioPueblo e inversores), Martín (masterplan) y el resto del equipo.

El equipo tiene que decidir en las próximas semanas qué puede ofrecer y a quién antes del **Gathering de febrero de 2027**, qué preparar para 2027–2028, y si parte de la tierra se vende o no. La caja alcanza hasta marzo de 2027 aproximadamente, así que el diseño tiene que levantar plata; también tiene que proteger la tierra y el procomún por décadas. Tu informe es el insumo para esa decisión y el paquete que va al estudio jurídico. Lo va a leer primero Gabriel (formación legal, conoce el proyecto), después el equipo (varios son nuevos tanto en cripto-economía como en regulación financiera argentina) y por último abogados que van a buscar cada afirmación sin respaldo.

Queremos dos cosas que tiran en direcciones opuestas a propósito:

- **Una lectura honesta de compliance** de la propuesta tal como está escrita: pieza por pieza, qué norma aplica, si estamos adentro, y con cuánta certeza lo decís.
- **La posición lícita más lejana**: para cada pared con la que choca el diseño, las estructuras que nos dejan conservar toda la agilidad y el atractivo para el capital que la ley realmente permite. El instinto del equipo es "empujar los límites"; tu trabajo es mostrar exactamente dónde están, para que empujemos con los ojos abiertos.

Qué significa acá "empujar los límites": buscamos estructuras donde cambia la **sustancia**, de modo que honestamente aplique otra norma (otro instrumento, otro emisor, otro público, otra jurisdicción, una vía regulada, una exención, un sandbox). No buscamos cambiar etiquetas. El derecho argentino mira a través de los nombres (CCyC art. 12 y el criterio de realidad económica de la CNV), y un diseño que depende de que nadie mire de cerca no nos sirve: los que saldrían lastimados son las familias que ponen USD 2–5 mil. Si un workaround es solo un cambio de vocabulario, decilo y descartalo. Si es real pero agresivo, conservalo y explicá qué lo sostiene y qué lo haría caer.

Animate igual a decirnos que somos **demasiado cautos**. El repo fue escrito a la defensiva por no abogados. Si una restricción que nos autoimpusimos (por ejemplo, transferibilidad cero en Argentina) es más estricta que la ley, ese hallazgo vale tanto como encontrar una infracción, porque libera espacio de diseño.

### 2. Qué leer y en qué orden

**La propuesta (repo `NS_Tokenomics`, en inglés).** Empezá por `AGENTS.md` y `00 - README.md` (convenciones, marcadores, reglas de privacidad: seguilas). Después:

| Orden | Archivo | Para qué |
|---|---|---|
| 1 | `06 - Legal Friction Map.md` | Nuestra lista de fricciones legales (L1–L38), cada una con un camino propuesto. Es lo principal que vas a auditar |
| 2 | `01 - Context and Constraints.md` | La tierra, las paredes legales como las entendíamos al 29-09-2026, cronograma |
| 3 | `16 - Call 2026-10-12 …`, `18 - Hybrid model …` | Dónde está hoy la discusión del equipo: vender o no algunos lotes, y las cinco cosas que "híbrido" puede significar |
| 4 | `17 - Lighthouse Constitution and Rights of Nature (draft).md` | Los derechos de la tierra que queremos fijar y en qué instrumentos los anclamos |
| 5 | `04 - MVP February 2027 (The Hatch).md` | Lo que queremos lanzar en febrero: Pase Fundador (RAIZ v0), Fondo Común, créditos |
| 6 | `15 - Micro-investor offer …` y `12 - Round Inputs …` §3–4 | La oferta de tickets chicos y a quién se le puede ofrecer qué |
| 7 | `09 - Investor Value Model …` | El capital stack y qué recibe cada tipo de inversor |
| 8 | `03 - Long-Term Vision.md` (§1–3, §7), `05 - Community Token Templates.md`, `10 - Governance Primitives (options).md` | Estado objetivo: capas, familias de tokens, kits de comunidad, reglas de voz, invariantes I1–I8 |
| 9 | `07 - Open Questions and Research Backlog.md`, `13`, `14` | Qué está decidido, qué está abierto |

**La bóveda de Gabriel.** Primero hacé un inventario. Buscá en particular: la investigación del 29-09-2026; todo lo que haya sobre la estructura DRS/fideicomiso con Lavima y BioPueblo; la Ordenanza 173/2026 de Mainqué (texto completo si está); presupuestos y memos de abogados; el memo de jurisdicción del 27-09-2026; el term sheet o LOI con BioPueblo; el estado de aprobación de Chacras de Soluna; y la transcripción de la llamada del 12-10-2026. Listá qué encontraste y qué esperabas encontrar y no estaba. El material de la bóveda es contexto del equipo, igual que el repo: útil, pero no es autoridad sobre lo que dice la ley.

**El documento de Franz** (ver §6). Leelo después del repo, para poder comparar.

Si no podés leer alguna de estas fuentes, decilo al principio del informe y seguí con lo que tengas. No rellenes el hueco suponiendo lo que dice el documento.

### 3. La propuesta en una página (orientación; la fuente es el repo)

- **La tierra de Lighthouse no se vende** (decisión del 02-10-2026, hoy en discusión: ver §5 B). Lavima (dueña) otorga un *derecho real de superficie* por macrolote a un **fideicomiso**; una entidad **Guardiana** es titular de servidumbres ecológicas perpetuas y del Fondo Común. Las comunidades reciben **licencias de uso**, no propiedad.
- **Tres potes de plata, tres envoltorios, sin mezclar:**

| Pote | Instrumento | Público | Qué recibe el titular |
|---|---|---|---|
| Empresa (holding de NetX, saliendo de Próspera hacia Uruguay / Wyoming / Delaware, sin definir) | **SAFE**, tickets de USD 5 mil, USD 375–500 mil | ~75–100 personas, incluidos residentes argentinos | Equity de riesgo |
| Procomún (Guardiana / Fondo Común) | **RAIZ**. En febrero de 2027, un **Pase Fundador** intransferible en tres niveles (USD 300 / 1.500 / 5.000) | Cualquiera, incluidos extranjeros | En especie: créditos consumibles de estadía y de bienes comunes (30% del precio en 3 años), una persona una voz sobre la asignación del fondo, reconocimiento de fundador |
| Tierra (fideicomiso Lighthouse) | **Unidades de fideicomiso**, privadas, ≤35 adquirentes por emisión | Family offices, inversores regenerativos | Ingresos por licencias y tarifas; salida por cesión de unidades |

- **Más adelante (RAIZ v2):** posiblemente transferible solo entre miembros admitidos, en "doble riel" (pase intransferible para residentes argentinos vía la Guardiana argentina; token de utilidad transferible para no residentes vía una entidad sin fines de lucro offshore), y vales comunitarios circulando en un pool de compromisos.
- **Micro-inversores (USD 2–5 mil):** un paquete "Founding Circle" de dos contratos separados, un SAFE y un Pase Fundador.
- **Constitución:** un texto único con los derechos de la tierra (tomados de OASA y de la Declaración Universal de los Derechos de la Madre Tierra), incorporado como anexo a la escritura, al fideicomiso, a las servidumbres, al estatuto de la Guardiana y a cada licencia.

### 4. Qué es fijo y qué tenés que cuestionar

Estos son **valores de diseño**. No son conclusiones legales y no se relajan; tomalos como instrucciones del cliente. Si encontrás que alguno es jurídicamente imposible de sostener, es un hallazgo de primera línea.

1. **El diodo.** Ningún token, fondo, comunidad o instrumento de inversión puede gravar, dar en garantía ni vender la tierra. Los derechos fluyen hacia arriba; la deuda y el recurso nunca bajan. (La parte "ni vender" está hoy en discusión dentro del equipo para una zona acotada: analizala en el bloque B sin darla por resuelta en ningún sentido.)
2. **Tres potes, nunca mezclados.** La plata del procomún nunca es ingreso de NetX ni capital inmobiliario.
3. **Los asuntos de los residentes se deciden una persona, un voto.** La plata no compra esa voz.
4. **Los derechos de la tierra van primero** y tienen que sobrevivir a NetX.

Estas son **hipótesis legales que adoptamos por seguridad**. Poné a prueba cada una. Pueden estar bien, ser demasiado estrictas o quedarse cortas:

- RAIZ tiene que ser pura utilidad, sin expectativa de ganancia; los retornos viven solo en el SAFE y en las unidades de fideicomiso. (Mientras lo analizás: en lo que escribas, no hagas pronósticos de precio ni lenguaje promocional de rendimiento sobre RAIZ. Analizar si un rasgo crea expectativa de ganancia en sentido jurídico es justamente el punto.)
- Nada de lotes, prioridades ni reservas de parcelas antes de la aprobación municipal (lo atribuimos a la Ordenanza 173/2026 de Mainqué, arts. 41–46).
- No se filtra por creencias o valores, solo por conducta y contribución (Ley 23.592).
- Transferibilidad cero del pase en Argentina (lo atribuimos a "activo virtual", Ley 25.246 art. 4 bis, y al régimen PSAV).
- Los créditos tienen que ser de emisor único, circuito cerrado, con vencimiento y sin rescate en dinero.
- Límite de oferta privada de 35 adquirentes por emisión, 15 no calificados, sin medios masivos (RG CNV 1016/2024, modificada por la RG 1088/2025: además, hasta 50 potenciales inversores por reunión, 30 invitaciones a no calificados y reventa bloqueada 3 o 6 meses).
- Un beneficiario extranjero hace tributar a todo el fideicomiso; los extranjeros no pueden adquirir tierra rural ribereña (LIG art. 73; Ley 26.737, **vigencia en disputa**: verificarla primero).

Tratá todo número de norma de este repo y del documento de Franz como **no verificado hasta que hayas visto el texto primario**. En esta materia las resoluciones cambian rápido, y ambos documentos se escribieron en parte desde fuentes secundarias y memoria de modelos.

### 5. Preguntas de investigación

Recorré los bloques. En cada uno: primero establecé la norma desde fuentes primarias, vigente hoy; después ubicá nuestro diseño frente a ella; después explorá el margen de maniobra. Las "vías a testear" salen de conocimiento general, no de investigación: son pistas, algunas no llevarán a nada, y sumá las tuyas.

**A. Territorio y jurisdicción (hacelo primero; de esto dependen otras respuestas)**
- El documento de Franz dice que la tierra está sobre la **margen sur** del río Negro y plantea la duda de si el macrolote cae dentro del ejido de Mainqué (menciona El Cuy y General Roca). Toda nuestra pared de "sin lotes antes de la aprobación" descansa en una ordenanza de Mainqué. ¿Qué municipio y qué ordenanzas rigen el Macrolote 7? ¿Qué dicen exactamente los arts. 41–46 de la Ordenanza 173/2026, y alcanzan a ofertas hechas online o en el exterior?
- **Chacras de Soluna** (barrio vecino de BioPueblo): según la llamada, su subdivisión ya tiene el trámite municipal hecho; la bóveda de Gabriel indica que la aprobación definitiva sigue pendiente. ¿En qué estado exacto está, y qué se puede ofrecer, publicitar y firmar hoy sobre esos lotes?
- Capa provincial: subdivisión y mensura; cambio de uso de suelo rural y unidad económica agraria; Código de Aguas y DPA (permisos de perforación, línea de ribera); camino de sirga (CCyC art. 1974); evaluación de impacto ambiental (Franz cita la Ley M 3266); impuesto de sellos sobre fideicomisos, cesiones y contratos de membresía.
- Ley 14.005 y Decreto 95/2024 [verify]: qué los dispara exactamente, y si alcanzan a un **crédito a cuenta de un lote futuro** o a una "prioridad" sin parcela identificada.
- Reclamos indígenas o consuetudinarios sobre la parcela o su entorno (Convenio 169 OIT; CN art. 75 inc. 17; ley provincial).

**B. Estructura de la tierra: no vender, vender algo, o un punto intermedio**
El repo decidió el 02-10 que las hectáreas de Lighthouse no se venden. En la llamada del 12-10 Franz propuso un modelo mixto (vender algunos lotes para financiar el arranque) y su documento recomienda Propiedad Horizontal Especial con servidumbre ambiental. Gus objeta que un lote vendido sale de nuestra gobernanza, complica el marketing y la burocracia. Quedó sin decidir, y el agrimensor recibe el masterplan en la primera quincena de noviembre. El equipo necesita la comparación legal de las cinco variantes de `18 - Hybrid model …`:
- **H0** híbrido a escala BioPueblo (BioPueblo vende sus lotes; Lighthouse es procomún; NetX refiere compradores). **H1** dos o tres lotes de Soluna comprados por gente cercana como base de operaciones. **H2** zona de venta dentro del 7A. **H3** derecho real sin vender la tierra. **H4** licencias largas y cedibles.
- Para **H2**: ¿el régimen de conjunto inmobiliario (CCyC arts. 2073–2086) está siquiera disponible acá (suelo rural, cerramiento exigido, escala)? Si el fideicomiso solo tiene un derecho de superficie, ¿puede vender lotes en dominio, o tendría que vender el dueño (Lavima / BioPueblo)? ¿Qué le hace al diodo? Tiempos y costos reales hasta poder firmar boletos.
- Para **H3**: ¿puede el superficiario afectar lo construido a propiedad horizontal y transmitir unidades como inmuebles independientes por el plazo del DRS (CCyC art. 2120 [verify])? ¿Esas unidades son hipotecables, y se puede preservar el diodo por contrato o en el título del DRS? Usufructo, uso y habitación (CCyC 2129–2161) como alternativas.
- Para **H4**: ¿qué figura lleva mejor la licencia? ¿Cuán frágil es un derecho personal (insolvencia del fideicomiso, fin del plazo de 30 años del fideicomiso, fin del DRS, herederos y acreedores del licenciatario)? ¿Se puede ceder la posición con consentimiento de la Guardiana, y qué pasa si esa cesión se registra con un NFT (ver bloque D)?
- **Perpetuidad.** Queremos que la protección "vaya a infinito". El DRS dura hasta 70 años y el fideicomiso hasta 30. ¿Qué instrumento lleva la protección después? ¿Quién recibe la tierra y las mejoras al final, y puede pactarse hoy con el dueño que el destino sea una entidad con el mismo fin (cláusula de sucesión, art. 11 del borrador de Constitución)?
- **Servidumbres.** ¿Puede una servidumbre ambiental ser verdaderamente perpetua en derecho argentino, y necesita fundo dominante (Franz la arma como servidumbre predial con la reserva como dominante; una servidumbre personal a favor de una persona jurídica podría tener plazo máximo, CCyC art. 2182 [verify])? ¿Qué implica para quién tiene que ser la Guardiana y qué tiene que poseer? ¿Hay en Río Negro legislación de reservas privadas o servidumbres de conservación que sea más fuerte?
- **Fiduciario:** sociedad argentina de NetX vs. fiduciario independiente (nuestro L21); obligaciones UIF del fiduciario.
- **Vehículo offshore dueño de la tierra** (modelo TDF: sociedad de propósito único controlada por una asociación suiza): ¿es viable para tierra rural argentina frente a la Ley 26.737 y sus límites a titularidad extranjera?
- **Comisión por venta de lotes ajenos (H0):** si la plataforma de NetX ayuda a vender lotes de BioPueblo y cobra comisión, ¿es corretaje inmobiliario que exige matrícula provincial? ¿Qué forma lícita tiene (acuerdo de referidos, servicio de marketing, corredor matriculado asociado)?

**C. El Pase Fundador y RAIZ como no-valor negociable**
- Aplicá la Ley 26.831 art. 2 y los criterios vigentes de la CNV al pase tal como está en `04` §2, rasgo por rasgo: precio por niveles, 30% en créditos, escalones de precio por cohorte, traspaso a un futuro RAIZ, reconocimiento de fundador, voz. ¿Qué rasgos, solos o combinados, lo acercan a valor negociable? Nuestro L15 teme que el traspaso se parezca a un SAFT: ¿es así?
- El "Crédito de Conversión" de Franz le da a un ticket de USD 5.000 un crédito de USD 5.500 contra un lote futuro, y a uno de USD 10.000, USD 11.500. Evalualo en sus propios términos: ¿un crédito mayor que el precio pagado, aplicable a tierra, es expectativa de ganancia? ¿Es preventa de lotes? Nuestro L27 rechazó una versión más suave.
- **Vía a testear:** el mismo descuento, pero aplicable solo a lotes de un barrio **ya aprobado** vendidos por su dueño (Soluna), o a la cuota de ingreso de una licencia. ¿Cambia el análisis?
- **Destino de la plata.** En la llamada se describió la plata de los tickets como caja para que NetX siga operando. Si el ticket lo emite una sociedad comercial y da estadías futuras, ¿qué es jurídicamente (servicio prepago, mutuo, aporte)? ¿Qué cambia si lo emite la Guardiana?
- En la práctica, ¿qué divulgaciones, redacción y conducta de marketing pesan más? Buscá sanciones, advertencias o criterios publicados de la CNV sobre tokens de utilidad, membresías y preventas desde 2023.
- **Vías a testear:** ¿existe alguna posición escrita de la CNV, ingreso a sandbox o mecanismo de consulta para obtener certeza previa sobre un pase de utilidad? ¿Podría emitirse lícitamente una versión de RAIZ con derechos económicos por una vía regulada, en lugar de evitarla (bloque F)?

**D. Transferibilidad, activos virtuales y régimen PSAV**
Acá sospechamos que podemos estar siendo demasiado cautos, y que Franz puede estar siendo demasiado laxo. Franz propone un ERC-1155 transferible con lista blanca ligada a identidad, reventa dentro de la plataforma como "cesión de posición contractual" y una tasa del 3% al procomún. Gus, por su parte, imagina a largo plazo un NFT que funcione como **llave de una casa** y que el titular pueda pasar a otra persona, y tokens fungibles que den días por año.
- ¿Qué convierte algo en *activo virtual* hoy (Ley 25.246 modificada por Ley 27.739; normas CNV vigentes sobre PSAV)? ¿Un registro on-chain **intransferible** queda afuera? ¿Un token transferible **solo entre miembros admitidos con KYC** queda adentro?
- ¿Quién es PSAV: el emisor de su propio token, quien opera el portal donde ocurren las reventas, quien cobra la tasa? Si el emisor no es PSAV por el solo hecho de emitir, ¿qué actividad lo convierte?
- ¿Una cesión de un contrato de membresía o de una licencia, registrada por la asociación, es jurídicamente distinta de una transferencia de token si el resultado económico es el mismo? ¿Qué haría que la diferencia sea real y no cosmética?
- ¿Una regla de **reventa sin ganancia** (solo al precio pagado, o con el excedente al Fondo Común) cambia el análisis de valor negociable?
- El doble riel (`06` §2): ¿puede una entidad sin fines de lucro offshore vender un token de utilidad transferible a no residentes y donar lo recaudado a la Guardiana argentina sin "dirigirse" a Argentina? Compará Suiza (práctica FINMA sobre utility tokens), Uruguay (ley de activos virtuales y regulación del BCU), Liechtenstein (TVTG) y el tratamiento de utility tokens en MiCA para compradores europeos. ¿Cómo tienen que ser el geobloqueo y el KYC para que cuenten?

**E. Créditos, vales y pagos**
- Créditos de circuito cerrado emitidos por la Guardiana y canjeados por bienes que la Guardiana compra a las comunidades (`04` §5): ¿quedan fuera de las normas del BCRA sobre proveedores de servicios de pago y de cualquier regulación de prepagos o gift cards? ¿El **vencimiento** a 12 meses es oponible bajo la Ley 24.240 y las reglas de cláusulas abusivas, o es un riesgo?
- Vales comunitarios persona a persona (patrón Grassroots Economics, `05` P1): ¿qué régimen aplica, si alguno? ¿Hay un marco utilizable desde clubes de trueque, mutuales o cooperativas?
- Créditos de estadía vs. tiempo compartido (CCyC arts. 2087–2102; Ley 26.356): ¿dónde está la línea? Los tickets de Franz dan "10 noches por año durante 4 años"; los nuestros, un saldo consumible; la idea de "30 tokens = 30 días" viene del modelo TDF. ¿Cuáles son tiempo compartido? ¿Cuánto pesa registrarse en serio como tiempo compartido u operador turístico, por si hacerlo bien es el mejor camino?
- Recibir plata del exterior en una entidad sin fines de lucro argentina: normas cambiarias **como están hoy** (cambiaron mucho; verificá), deberes UIF de origen de fondos, rieles prácticos.

**F. Levantar capital lícitamente de muchos inversores chicos**
Este es el centro de "atractivo para el capital". La respuesta actual del repo es un SAFE privado más unidades de fideicomiso privadas, ambos topeados por el puerto seguro de oferta privada. Averiguá si hay puertas más anchas.
- Confirmá el puerto seguro de oferta privada vigente: números, cómo se cuenta "por emisión" y la acumulación en el tiempo, qué es medio masivo (el equipo habla en eventos públicos: L28) y cómo se define inversor calificado.
- El SAFE: ¿es exigible y utilizable con inversores residentes argentinos cuando el emisor es un holding extranjero? ¿Cómo se apilan las reglas argentinas de oferta privada con las del domicilio del emisor (EE.UU.: Reg D / Reg S / Reg CF para Wyoming o Delaware; Uruguay)? ¿Qué implica cada jurisdicción para 75–100 tenedores chicos (límites de cap table, impuestos, costo)? Nuestro L20 sobre un "×2" fijo.
- **Vías a testear**, cada una con requisitos, costo, plazos y límites de inversores: el régimen de *plataformas de financiamiento colectivo* (Ley 27.349 Título II y normas CNV vigentes) para tickets de USD 2–5 mil; los regímenes simplificados o de autorización automática de oferta pública de la CNV para emisores chicos y para fideicomisos financieros [verificar que existan como suponemos]; un **fideicomiso financiero tokenizado** vía PSAV registrado bajo el régimen de tokenización de la CNV (el repo cita RG 1069/2025 → RG 1150/2026 y un sandbox hasta el 31-12-2027: verificá, y decinos si hay una fecha que perderíamos por esperar); fondos comunes cerrados inmobiliarios; una **cooperativa** (Ley 20.337) o mutual como vehículo del procomún o de las comunidades, dado que se gobiernan un asociado un voto y pueden devolver excedentes en proporción al uso; SAS de propiedad responsable con acción de oro (nuestra pregunta 6 en `06` §3), y el estado real de la etiqueta "BIC" que usa Franz (creemos que no hay ley nacional BIC vigente [verify]).
- Inversores extranjeros en el fideicomiso: ¿es cierto que un beneficiario extranjero cambia el tratamiento fiscal de todo el fideicomiso, y qué estructuras de uso corriente lo resuelven (un feeder, un vehículo local)? Estado al día de la reforma de la Ley 26.737.
- Para cada puerta: ¿puede convivir con el diodo y con la regla de los tres potes?

**G. El Fondo Común y la Guardiana**
- Franz ubica el Fondo Común como una "subcuenta inembargable" **dentro del fideicomiso inmobiliario**, alimentada por 3% de la venta de lotes, 5% de los tickets, 3% de las reventas y 10% de la utilidad de hospitalidad, y hace que una sociedad comercial operadora emita los tickets. El repo lo ubica en una Guardiana sin fines de lucro, separada del fideicomiso de tierra y de toda sociedad. Compará en: protección patrimonial, quién lo controla, impuestos, qué pasa cuando termina el fideicomiso, y si la versión de Franz mezcla los potes. ¿Es correcta su afirmación de inembargabilidad? ¿Un **fideicomiso de administración** separado para el procomún da la misma protección sin mezclar?
- Forma de la Guardiana: asociación civil, fundación, cooperativa o fideicomiso. ¿Cuál puede tener una categoría de miembros con derecho estatutario de asignación (nuestra pregunta 1), cuánto tarda la inscripción en Río Negro, y si un patrocinador fiscal puede cubrir hasta febrero?
- Tratamiento fiscal de los ingresos del pase (cuota o donación vs. servicios; IVA, exención de Ganancias, IIBB, Sellos) y del titular.
- Voz: el repo fija una persona una voz; Franz da 1 voto al ticket de USD 5 mil y 3 al de USD 10 mil. Más allá de nuestra regla de diseño, ¿ponderar votos consultivos por dinero tiene consecuencias legales (para el análisis de valor negociable, o para el derecho asociativo)?

**H. Personas: trabajo, admisión, datos**
- Trabajo que gana RAIZ, créditos, "semillas" o un camino a una licencia (L12; en la llamada: comprometer 20–40 horas por mes a cambio de un token de acceso): recalificación como relación laboral, ley de voluntariado, seguros, impuestos sobre ingresos en especie. ¿Cuál es el diseño lícito más generoso?
- Admisión y exclusión por conducta y contribución; sanciones graduadas; la idea de Franz de suspender la visibilidad en la plataforma como sanción. Límites de la Ley 23.592, del derecho del consumidor y del derecho asociativo.
- Datos personales en registros de presencia, trabajo y reputación (Ley 25.326 y cualquier reforma vigente); KYC biométrico, que propone Franz.

**I. Comunicación**
- Un conjunto práctico de reglas para charlas públicas, el sitio web y conversaciones uno a uno con inversores, a la luz de los bloques A, C y F: qué se puede decir de la tierra, los lotes (de Lighthouse y de Soluna, por separado), el pase, el SAFE y las unidades, a quién y por qué canal. El equipo tiene charlas en BitConf (30–31 de octubre de 2026) y otros eventos.

**J. Constitución y derechos de la naturaleza**
Leé `17 - Lighthouse Constitution and Rights of Nature (draft).md`. No queremos pelear el reconocimiento de un recurso natural como sujeto de derecho: está fuera de nuestro alcance. Queremos **fijar esos derechos como deberes** en cada instrumento que da poder sobre la tierra, de modo que dentro de nuestro perímetro funcionen como una constitución ("como si fuésemos nuestra propia jurisdicción", que en la práctica significa autorregulación privada dentro del orden público).
- Capa por capa de la tabla de `17` §3 (servidumbres, título del DRS, contrato de fideicomiso, estatuto de la Guardiana, licencias, reglamentos): ¿qué puede obligar cada instrumento, a quién, por cuánto tiempo y con qué remedio? ¿Dónde conviene poner cada derecho para que dure más?
- ¿Qué apoyo da el derecho vigente (CCyC arts. 14 y 240, Ley 25.675, CN art. 41, Constitución y leyes de Río Negro, jurisprudencia argentina que haya reconocido derechos a ecosistemas o animales)? Usalo para reforzar las cláusulas, no para proponer litigios.
- **Cláusulas pétreas:** ¿cómo se logra en derecho argentino que ciertas reglas no puedan modificarse (o solo con doble llave: asamblea más Guardianes de la Naturaleza)? ¿Qué vale más: estatuto, servidumbre, cargo en la escritura, derecho de veto de un tercero?
- **Veto de los Guardianes de la Naturaleza** y del Consejo de Regeneración: ¿qué forma jurídica puede tener un veto que no dependa de quien controla la entidad?
- **Licencia condicionada a conducta ecológica**: ¿es ejecutable terminar una licencia donde vive gente por incumplir los principios? Límites de consumidor, vivienda y debido proceso; diseño de sanciones graduadas y resolución de disputas (mediación, arbitraje).
- **Sucesión:** si NetX o la Guardiana fallan, que la custodia pase a una entidad con el mismo fin y la tierra no vuelva al mercado (art. 11 del borrador). ¿Cómo se instrumenta, dado que la tierra es de un tercero?
- **Monitoreo automatizado:** un agente de IA que señala incumplimientos y pausa decisiones hasta que resuelvan personas. Límites por datos personales y por decisiones automatizadas.
- En un lote vendido (H2), ¿cuánto de todo esto sobrevive? Compará con lo que logran hoy los reglamentos de barrios cerrados patagónicos que exigen energías renovables y materiales naturales (lo mencionó Martín).

### 6. El documento de Franz y la llamada del 12-10: cómo tratarlos

El documento de Franz es una salida de deep research de Gemini producida el mismo día de la llamada, a partir de su transcripción. Se escribió sin acceso a este repo ni a la investigación del 29-09. Tratalo como una segunda propuesta de un compañero de equipo, con buenas ideas y con los límites de cómo se hizo. Su registro seguro ("neutraliza la intervención de la CNV", riesgo "mínimo", "inexpugnable") es del modelo, no un hallazgo jurídico, y muchas de sus citas van a blogs, revistas notariales de otras provincias, Wikipedia y al menos una tesis sin relación. Verificá sus afirmaciones como las de cualquiera.

Detrás del documento hay una necesidad real que el informe tiene que atender: **caja en el corto plazo**. Franz no discute el procomún como destino; pide un camino que traiga liquidez pronto y compradores que quieren escritura. Una respuesta que solo diga "no se puede" no le sirve al equipo.

Puntos donde se aparta del repo, sobre los que tenés que pronunciarte uno por uno:

| # | Documento de Franz | Repo | Por qué importa |
|---|---|---|---|
| 1 | Vende lotes (1.500–5.000 m²) bajo PH Especial; boletos Ley 14.005 | La tierra de Lighthouse no se vende; DRS + licencias | Principio central; bloque B |
| 2 | El ticket lleva un **crédito contra un lote futuro**, mayor que el precio pagado, más prioridad de compra | Sin lotes, prioridades ni reservas antes de la aprobación | Preventa de lotes y expectativa de ganancia; bloques A y C |
| 3 | Tickets emitidos por una sociedad comercial operadora (S.A./S.A.S. "BIC") | Pase emitido por la Guardiana sin fines de lucro | De quién es el ingreso; regla de los tres potes |
| 4 | Fondo Común = subcuenta del fideicomiso inmobiliario | Fondo Común en la Guardiana | Mezcla de potes; bloque G |
| 5 | ERC-1155 transferible, lista blanca, reventa operada por la plataforma con tasa del 3%, desde el día uno | Intransferible en Argentina en v0; transferencias entre miembros solo como opción posterior (L26) | Exposición PSAV y de valores; bloque D |
| 6 | "10 / 22 noches por año durante 4 años" | Saldo de créditos consumible | Tiempo compartido; bloque E |
| 7 | 1 voto por USD 5 mil, 3 votos por USD 10 mil | Una persona, una voz | Regla de diseño 3; bloque G |
| 8 | No menciona el DRS, la Ordenanza 173/2026, los límites de oferta privada, los límites a extranjeros ni el SAFE | Son las paredes principales del repo | Hueco de cobertura |

Cosas del documento de Franz que al repo le faltan y que parecen valer la pena si se verifican: la pregunta de qué municipio tiene jurisdicción; permisos de agua del DPA y línea de ribera; camino de sirga; evaluación de impacto ambiental provincial; unidad económica agraria y cambio de uso de suelo; sellos; las ventajas de ejecutabilidad de los derechos reales frente a los contratos (cobro ejecutivo de expensas, cargas ambientales *propter rem*); la hoja de ruta de trámites por fases.

Si la transcripción del 12-10 está en la bóveda, usala para entender qué quiere cada persona. No la cites en extenso; citala por nombre y fecha.

### 7. Método y estándar de prueba

- **Deciden las fuentes primarias.** Para ley nacional, InfoLEG / SAIJ / Boletín Oficial; para reguladores, los sitios de CNV, BCRA, UIF y ARCA; para Río Negro, el digesto de la Legislatura y el Boletín Oficial provincial; para Mainqué, el municipio o el Concejo Deliberante. Citá la norma, el artículo, un enlace y la fecha de consulta. Para cada norma confirmá que está vigente y anotá modificaciones posteriores.
- **Decí cómo lo sabés.** Usá los marcadores del repo en cada afirmación jurídica: **[C]** confirmado en una fuente primaria que leíste · **[S]** solo fuente secundaria · **[NC]** no pudiste confirmar · **[criterio]** tu razonamiento · **[verify]** tiene que revisarlo el estudio. Una afirmación que recordás pero no encontraste es [NC], por más seguro que te sientas. Si no encontrás un artículo, una resolución o un caso, escribí que no lo encontraste. Un informe con huecos honestos le sirve al estudio; una sola cita inventada lo vuelve inutilizable.
- **Separá cuatro capas** en cada respuesta: el texto de la norma; cómo la aplicó el regulador (sanciones, criterios, precedentes como los fideicomisos inmobiliarios tokenizados que menciona el repo); qué dice la doctrina; y tu propia inferencia.
- **Hacé la lectura adversarial.** Para cada camino compliant, escribí el párrafo que escribiría en contra un inspector de la CNV, una oficina de defensa del consumidor o el abogado de un actor, leyendo juntos el contrato y el marketing. Después decí si el camino sobrevive.
- **La fecha de hoy importa.** La línea de base es el 29-09-2026; verificá qué cambió desde entonces y todo lo que tenga plazo (ventanas de sandbox, proyectos de ley, regímenes transitorios).
- Si tu entorno permite investigadores en paralelo, dividí por bloque (A–J) y hacé una pasada separada que verifique las citas del informe final contra las fuentes. Hacé el bloque A primero, porque puede cambiar los demás.
- Seguí las reglas de privacidad del repo: sin datos personales, sin citas extensas de transcripciones privadas ni de decks de terceros.

### 8. Qué entregar

Un documento Markdown en español (va al estudio jurídico), con un resumen ejecutivo en inglés de una página para los colaboradores no hispanohablantes, siguiendo las convenciones del repo (resumen 🌱 en lenguaje llano arriba, notas al pie, leyenda ✅ 🧨 🏴‍☠️ ❓ y una sección final **"Sources & logic used"**). Guardalo en el repo como `19 - Legal Deep Research (compliance and room to manoeuvre).md` en tu rama. Escribí para alguien que no vio tu proceso: oraciones completas, términos definidos, la conclusión antes del razonamiento.

1. **🌱 En una frase** y después **los diez hallazgos que cambian el diseño**, del más al menos consecuente. Incluí dónde nos pasamos, dónde somos más cautos de lo necesario y dónde no pudiste averiguar.
2. **Qué leíste y qué no pudiste leer.**
3. **Tablero de compliance.** Una fila por elemento de diseño (usá la numeración L1–L38 de `06` y agregá filas para lo que falte): la norma, el estado de la norma ([C]/[S]/[NC]), dónde queda nuestro diseño, y una nota en esta escala con una oración de justificación:
   - **A** compliant como está · **B** compliant si se cumplen condiciones concretas (listalas) · **C** defendible pero discutido; requiere dictamen escrito · **D** no compliant como está; existe una alternativa real · **E** no compliant; no se encontró camino · **?** no se pudo determinar.
   No lo comprimas en un porcentaje único. El resumen honesto es el conteo de filas por nota, por separado para el MVP de febrero y para la visión de largo plazo.
4. **Margen de maniobra.** Para cada pared, la escalera de opciones de la más conservadora a la más ambiciosa. Para cada escalón: qué cambia en la sustancia, qué norma aplica entonces, precedentes, costo y tiempo, qué le hace al diodo y a los tres potes, la lectura adversarial y el riesgo residual. Marcá cada escalón ✅ (práctica establecida), 🏴‍☠️ (real pero agresivo; decí qué lo sostiene) o ✗ (solo cambio de etiqueta; descartado, y por qué).
5. **El modelo híbrido.** Las cinco variantes H0–H4 de `18`, con tu veredicto legal de cada una, tiempos y costos, y qué necesita saber Martín antes de llevar el masterplan al agrimensor.
6. **Franz vs. repo**: la tabla del §6 con tu pronunciamiento fila por fila y una síntesis propuesta que atienda la necesidad de caja.
7. **Constitución**: para cada artículo del borrador de `17` §4, el instrumento donde conviene anclarlo, su fuerza real y la redacción que sugerís revisar.
8. **Configuraciones recomendadas.** (a) Qué podemos ofrecer en el Gathering de febrero de 2027; (b) el stack lícito más atractivo para 2027–2028, incluida la mejor vía para inversores de USD 2–5 mil; (c) qué tendría que cambiar en la ley o qué aprobación necesitaríamos para ir más lejos. Para cada una, qué tiene que dejar de decir o hacer el equipo desde ya.
9. **Ruta crítica**: presentaciones, inscripciones y dictámenes necesarios, en orden, con duraciones y costos aproximados donde puedas respaldarlos.
10. **Preguntas para el estudio jurídico**: las que solo cierra un dictamen firmado, en orden de prioridad, cada una con el contexto que un abogado necesita para presupuestarla.
11. **Ediciones propuestas al repo**: correcciones a `06` (filas a cambiar, agregar o borrar, con las citas corregidas), entradas nuevas para `07`, y cualquier regla de diseño de `AGENTS.md` que tus hallazgos pongan en duda. Listalas; Gabriel las aplica en el pull request.
12. **Sources & logic used.**

### 9. Cómo se ve un buen resultado

Un buen informe le permite a Gabriel entrar a una reunión con el estudio y dedicar la hora a las cinco preguntas que de verdad están abiertas, en vez de a establecer los hechos. Le da al equipo una base común para decidir el modelo híbrido sin que gane quien habla más fuerte. Cambia al menos algunas cosas que creíamos. Nunca le dice al equipo que algo es seguro apoyándose en un blog, y nunca le dice que algo está prohibido sin mostrar la norma. Donde la respuesta honesta es "depende de la discrecionalidad de un regulador", dice quién decide, cómo preguntarle y qué debería hacer el equipo mientras tanto.

---

## Sources & logic used

- Pedido de Gus, 13-10-2026: un prompt que Gabriel pueda correr contra su bóveda para producir un deep research legal sobre el nivel de compliance de la tokenomics y sobre workarounds lícitos que la mantengan ágil y atractiva para el capital; versión en español para enviar aparte.
- Este repositorio (v0.4 en preparación): archivos 00, 01, 03, 04, 05, 06, 07, 09, 10, 12, 15, 16, 17, 18 y `AGENTS.md`. El resumen del §3 y la división "fijo / a cuestionar" del §4 reformulan esos archivos.
- Llamada "Plataforma | Tokenomics y MicroFunding", 12-10-2026 (transcripción Fathom, privada), resumida en [[16 - Call 2026-10-12 (hybrid model, inputs and actions)]].
- Google Doc de Franz *"Arquitectura Legal, Financiera, Tokenómica y de Gobernanza para el Desarrollo Territorial Regenerativo: Barrio Lighthouse VRN (Biopueblo)"* (deep research de Gemini, 12-10-2026, leído el 13-10-2026). La tabla comparativa del §6 es nuestra lectura [criterio].
- OASA, *Principles of Regeneration and Land Stewardship* v1.0 (2022) y *OASA Constitution 2025*; Declaración Universal de los Derechos de la Madre Tierra (GARN), vía [[17 - Lighthouse Constitution and Rights of Nature (draft)]].
- Las "vías a testear" del §5 (PH sobre superficie, cooperativas, plataformas de financiamiento colectivo, regímenes simplificados de oferta pública, MiCA, fideicomiso de administración separado, plazo de las servidumbres personales, estado de BIC, corretaje, descuento sobre lotes ya aprobados, reventa sin ganancia) salen de conocimiento general, no de investigación [verify]: son pistas para quien investiga, no afirmaciones.
- Lógica: sustancia sobre forma (CCyC art. 12); auditar nuestra cautela tanto como nuestra exposición; fuentes primarias antes que memoria de modelos.
