class PasarelaPago: #Implementamos esta clase con los siguientes atributos procesoPago y verificarPago
    def procesoPago(self, monto): #Atributo procesoPago se usara como Abstracción
        pass  

    def verificarPago(self): #Atributo verificarPago se usara como Abstracción
        pass 

class PasarelaPagoTarjetaCredito(PasarelaPago): #Nuestra clase concreta abstraera los atributos de PasarelaPago realizando sus porpios servicios
    def procesoPago(self, monto):
        return f"Procesando el pago de {monto} con tarjeta de crédito." #Implementamos la abstracción

    def verificarPago(self): #Implementamos la abstracción
        return "Pago con tarjeta de crédito verificado con éxito."

class PasarelaPagoPaypal(PasarelaPago): #Nuestra clase concreta abstraera los atributos de PasarelaPago realizando sus porpios servicios
    def procesoPago(self, monto): #Implementamos la abstracción
        return f"Ejecutando la transferencia del pago de {monto} con PayPal."

    def verificarPago(self): #Implementamos la abstracción
        return "Pago con PayPal verificado con éxito."