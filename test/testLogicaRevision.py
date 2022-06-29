import unittest
from logica.logicaRevision import LogicaRevision

class test_ingresar_vehiculo (unittest.TestCase) :
    
    def test_registrar_liquidos (self):
        """Prueba de registro de niveles de liquidos"""
        resultado_registro = LogicaRevision.registrar_revision('2', 'UEV100', '1', '2', '3', '4')
        
        self.assertTrue(resultado_registro)
        
  
        