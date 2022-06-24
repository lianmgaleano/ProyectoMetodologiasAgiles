import unittest
from logica.logicaPersona import LogicaPersona

class TestLogicaPersona(unittest.TestCase) :

    def test_ingresar_mecanico (self):
        """Prueba de un registro  de un mecánico nuevo"""
        resultado_registro = LogicaPersona.registrar_persona('654321987', 'Pablo Arias', '2')

        self.assertTrue(resultado_registro)

    def test_ingresar_mecanico_existente (self):
        """Prueba de un registro de un mecánico existente"""
        resultado_registro = LogicaPersona.registrar_persona('654321987', 'Pablo Arias', '2')

        self.assertFalse(resultado_registro)

    def test_ingresar_dueno (self):
        """Prueba de un registro de un dueño nuevo"""
        resultado_registro = LogicaPersona.registrar_persona('654321987', 'Antonia Betancur', '1')

        self.assertTrue(resultado_registro)

    def test_ingresar_dueno_existente (self):
        """Prueba de un registro de un dueño existente"""
        resultado_registro = LogicaPersona.registrar_persona('654321987', 'Antonia Betancur', '1')

        self.assertFalse(resultado_registro)

    def test_ingresar_dueno_mecanico (self):
        """Prueba de un registro de un dueño nuevo que es mecánico"""
        resultado_registro = LogicaPersona.registrar_persona('987321456', 'Andrés Rios', '2')

        self.assertTrue(resultado_registro)

    def test_ingresar_dueno_existente (self):
        """Prueba de un registro de un mecánico nuevo que es dueño"""
        resultado_registro = LogicaPersona.registrar_persona('654147852', 'Mario Arias', '1')

        self.assertTrue(resultado_registro)    

    
