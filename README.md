Módulo de Personalizaciones CRM - Boom Solutions Odoo V18

Descripción Breve del Módulo
Este módulo personalizado extiende el módulo CRM nativo de Odoo 18 para añadir funcionalidades y campos adicionales al modelo crm.lead (Oportunidades/Leads), según los requisitos de la Prueba Técnica de Desarrollo Odoo V18. Su objetivo es mejorar la gestión de leads con información más detallada y un proceso de aprobación claro.

Funcionalidades Implementadas
El módulo añade las siguientes funcionalidades y campos a la vista formulario de Oportunidades:

Nuevos Campos Personalizados:

x_lead_category: Campo de selección (Selection) con opciones: 'residencial', 'empresarial', 'gubernamental'.
x_delivery_deadline: Campo de fecha (Date) que indica la fecha límite para procesar el lead.
x_approved_by: Campo Many2one a res.users que indica quién aprobó el lead. (Se rellena automáticamente al aprobar y es de solo lectura).
x_approved_date: Campo de fecha y hora (Datetime) que indica la fecha y hora de aprobación. (Se rellena automáticamente al aprobar y es de solo lectura).
x_duration_since_approved: Campo computado (Computed Readonly) que calcula el tiempo transcurrido desde la aprobación del lead.
x_installation_required: Campo booleano (Boolean) que indica si el lead requiere instalación técnica posterior.
x_installation_date: Campo de fecha (Date) para la fecha de instalación, visible solo si x_installation_required es True.
x_contract_reference: Campo de texto (Char) para una referencia de contrato.
x_support_required: Campo booleano (Boolean) que indica si el lead requiere soporte posterior.

Botón "Aprobar Lead":
Un botón (Button) en la cabecera del formulario de Oportunidad/Lead.
Al hacer clic, rellena automáticamente los campos x_approved_by (con el usuario actual), x_approved_date (con la fecha y hora actuales), y x_delivery_deadline (con la fecha actual, según la interpretación del requisito). Una vez aprobado, el botón se oculta y los campos de aprobación se vuelven de solo lectura.

Datos de Demostración:

Incluye un archivo demo_data.xml con dos registros de ejemplo de Oportunidades que contienen datos para los nuevos campos personalizados.

Pasos de Instalación
Clonar/Descargar el Repositorio:
Obtén el código de este módulo desde el repositorio de GitHub (el link que se entregaría).

Copiar al Directorio de Addons de Odoo:
Coloca la carpeta del módulo (por ejemplo, [tu_modulo]) dentro del directorio addons de tu instalación de Odoo 18.

Ejemplo de ruta: /path/to/odoo/odoo-server/addons/[tu_modulo]

Actualizar Lista de Aplicaciones en Odoo:

Inicia tu servidor Odoo.

Accede a tu base de datos con una cuenta de administrador.

Activa el Modo Desarrollador (yendo a Ajustes -> Activar el modo de desarrollador, en la parte inferior izquierda).

Ve a Aplicaciones.

Haz clic en "Actualizar lista de aplicaciones" (el botón con flechas circulares).

Instalar el Módulo:

En la barra de búsqueda de Aplicaciones, busca el nombre de tu módulo (por ejemplo, "Boom CRM Customizations" o el nombre que hayas definido en el __manifest__.py).

Haz clic en el botón "Instalar" junto a tu módulo.

Nota para datos de demostración: Para que los datos de demostración se carguen, es crucial que el módulo se instale en una base de datos limpia o se desinstale y se vuelva a instalar si ya estaba presente.

Cómo Probar el Módulo
Una vez instalado el módulo, puedes probar las funcionalidades de la siguiente manera:

Verificar Nuevos Campos:

Ve a la aplicación CRM.

Crea una nueva Oportunidad/Lead o abre un registro existente.

En la vista formulario, deberías ver una nueva sección llamada "Información Adicional de Oportunidad" con los campos Categoría de Lead, Fecha Límite de Entrega, Requiere Instalación, Fecha de Instalación, Referencia de Contrato y Requiere Soporte.

Verifica que los campos Aprobado por, Fecha de Aprobación y Duración desde Aprobación estén visibles, pero de solo lectura.

Probar el Botón "Aprobar Lead":

Abre una Oportunidad/Lead que no esté aprobada (asegúrate de que el campo Aprobado por esté vacío).

Deberías ver el botón "Aprobar Lead" en la parte superior del formulario (en la cabecera).

Haz clic en el botón "Aprobar Lead".

Verifica que los campos Aprobado por (rellenado con tu usuario), Fecha de Aprobación (con la fecha/hora actual) y Fecha Límite de Entrega (con la fecha actual, si así lo configuraste en el código Python de la acción) se hayan rellenado automáticamente.

El botón "Aprobar Lead" debería desaparecer una vez que los campos de aprobación estén llenos.

Verificar Chatter/Tracking:

En la misma Oportunidad/Lead, verifica que el Chatter (la sección de mensajes, actividades y seguidores) se muestre correctamente en el lado derecho de la pantalla. Si tu pantalla es muy pequeña, es posible que se desplace a la parte inferior debido al diseño responsivo de Odoo.

Verificar Datos de Demostración:

En la aplicación CRM, ve a la vista de lista de Oportunidades/Leads.

Deberías encontrar al menos dos nuevos registros (por ejemplo, "Oportunidad de Demostración - Proyecto X", "Oportunidad de Demostración - Servicio Y") que fueron creados por el demo_data.xml.

Abre uno de estos registros y verifica que los campos personalizados estén llenos con los valores definidos en el archivo demo_data.xml.