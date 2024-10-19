# EntregableProgram

## Clases

### 1. Casa

Esta clase representa una casa básica.

**Inputs:**

- `n_habitaciones` (int): Número de habitaciones. Valor por defecto: 1.
- `m_cuadrados` (int): Tamaño en metros cuadrados. Valor por defecto: 20.
- `propietario` (str): Nombre del propietario. Valor por defecto: vacío.
- `precio` (float): Precio de la casa. Valor por defecto: 50000.0.

**Métodos:**

- `__init__`: Inicializa una instancia de la casa con los valores indicados.
- `n_habitaciones` (propiedad): Devuelve el número de habitaciones.
- `m_cuadrados` (propiedad): Devuelve el tamaño en metros cuadrados.
- `propietario` (propiedad): Devuelve el nombre del propietario.
- `precio` (propiedad): Devuelve el precio de la casa.
- `mostrar_datos()`: Muestra los detalles de la casa (número de habitaciones, tamaño, propietario, precio).
  - **Output**: Una cadena de texto con la información detallada de la casa.
- `build_rooms(n_habitaciones, m_cuadrados)`: Añade habitaciones y metros cuadrados a la casa.
  - **Inputs**: Número de habitaciones a añadir (`n_habitaciones`) y tamaño en metros cuadrados (`m_cuadrados`).
  - **Output**: Actualiza los atributos de la casa y muestra un mensaje de confirmación.

### 2. PisoAlquiler (subclase de Casa)

Esta clase hereda de `Casa` y añade características específicas para pisos de alquiler.

**Inputs:**

- Hereda los atributos de `Casa`.
- `alquilerMensual` (float): Precio del alquiler mensual. Valor por defecto: 400.0.
- `arrendador` (str): Nombre del arrendador. Valor por defecto: vacío.

**Métodos:**

- Hereda los métodos de `Casa`.
- `alquilerMensual` (propiedad): Devuelve el alquiler mensual.
- `arrendador` (propiedad): Devuelve el nombre del arrendador.
- `mostrar_datos()`: Muestra los detalles del piso de alquiler junto con el alquiler mensual y el arrendador.
  - **Output**: Una cadena de texto con la información detallada del piso.
- `calcular_gastos()`: Calcula los gastos adicionales en base al número de habitaciones y metros cuadrados.
  - **Output**: Retorna el alquiler mensual más los gastos adicionales calculados (gastos extra).

### 3. Hotel (subclase de Casa)

Esta clase representa un hotel y añade características específicas como clientes y precio por noche.

**Inputs:**

- Hereda los atributos de `Casa`.
- `n_clientes` (int): Número de clientes actuales en el hotel. Valor por defecto: 5.
- `precio_por_noche` (float): Precio por noche por cliente. Valor por defecto: 20.0.

**Métodos:**

- Hereda los métodos de `Casa`.
- `n_clientes` (propiedad): Devuelve el número de clientes en el hotel.
- `precio_por_noche` (propiedad): Devuelve el precio por noche.
- `habitaciones_libres()`: Calcula el número de habitaciones disponibles.
  - **Output**: Retorna el número de habitaciones libres.
- `check_in(n_cliente)`: Registra clientes en el hotel, si hay suficientes habitaciones disponibles.
  - **Input**: Número de clientes a registrar (`n_cliente`).
  - **Output**: Actualiza el número de clientes y muestra un mensaje indicando las habitaciones restantes.
- `check_out(n_cliente)`: Registra la salida de clientes del hotel.
  - **Input**: Número de clientes que hacen check-out (`n_cliente`).
  - **Output**: Actualiza el número de clientes y muestra el número de habitaciones disponibles.
- `mostrar_datos()`: Muestra los detalles del hotel, incluyendo número de clientes y precio por noche.
  - **Output**: Una cadena de texto con la información detallada del hotel.
