class Usuario:
    TURNOS_VALIDOS: tuple[str, ...] = ("MANANA", "TARDE", "NOCHE")
    LONGITUD_MINIMA_CONTRASENA: int = 4

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        turno: str,
        usuario: str,
        contrasena: str,
    ) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.turno = turno
        self.usuario = usuario
        self.contrasena = contrasena

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificacion del usuario no puede estar vacia.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre del usuario no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def turno(self) -> str:
        return self._turno

    @turno.setter
    def turno(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El turno no puede estar vacio.")
        turno_normalizado = valor.strip().upper()
        if turno_normalizado not in self.TURNOS_VALIDOS:
            opciones = ", ".join(self.TURNOS_VALIDOS)
            raise ValueError(f"Turno no valido. Opciones: {opciones}")
        self._turno = turno_normalizado

    @property
    def usuario(self) -> str:
        return self._usuario

    @usuario.setter
    def usuario(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre de usuario no puede estar vacio.")
        # Se estandariza en mayusculas, igual que el codigo de producto.
        self._usuario = valor.strip().upper()

    @property
    def contrasena(self) -> str:
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La contrasena no puede estar vacia.")
        valor_limpio = valor.strip()
        if len(valor_limpio) < self.LONGITUD_MINIMA_CONTRASENA:
            raise ValueError(
                f"La contrasena debe tener al menos {self.LONGITUD_MINIMA_CONTRASENA} caracteres."
            )
        tiene_letra = any(caracter.isalpha() for caracter in valor_limpio)
        tiene_numero = any(caracter.isdigit() for caracter in valor_limpio)
        if not (tiene_letra and tiene_numero):
            raise ValueError("La contrasena debe combinar letras y numeros.")
        self._contrasena = valor_limpio

    def validar_credenciales(self, usuario: str, contrasena: str) -> bool:
        # Compara las credenciales ingresadas con las registradas para este usuario.
        return self._usuario == usuario.strip().upper() and self._contrasena == contrasena.strip()

    def convertir_a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "turno": self.turno,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
        }

    def __str__(self) -> str:
        return (
            f"Identificacion: {self.identificacion} | Nombre: {self.nombre} | "
            f"Turno: {self.turno}"
        )
