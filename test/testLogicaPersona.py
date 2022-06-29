import unittest
from logica.logicaPersona import LogicaPersona

class TestLogicaPersona(unittest.TestCase) :


    def test_ingresar_dueno (self):
        """Prueba de un registro de un dueño nuevo"""
        resultado_registro = LogicaPersona.registrar_persona('654321987', 'Antonia Betancur', '1')

        self.assertTrue(resultado_registro)
        

    def test_ingresar_dueno_existente (self):
        """Prueba de un registro de un dueño existente"""
        resultado_registro = LogicaPersona.registrar_persona('654321987', 'Antonia Betancur', '1')

        self.assertFalse(resultado_registro)

    

    
