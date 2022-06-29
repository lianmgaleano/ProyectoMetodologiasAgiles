import unittest
from logica.logicaVehiculo import LogicaVehiculo

class test_ingresar_vehiculo (unittest.TestCase) :
    
    def test_asignar_mecanico (self):
        """Prueba asignar mecánico"""
        resultado_registro = LogicaVehiculo.asignar_mecanico('UEV100', '123456789A')
        
        self.assertTrue(resultado_registro)
        
    def test_placa_inexistente (self):
        """Prueba placa inexistente"""
        resultado_registro = LogicaVehiculo.asignar_mecanico('MAP102', '123456789A')
        
        self.assertTrue(resultado_registro) 
        
    def test_documento_inexistente (self):
        """Prueba documento inexistente"""
        resultado_registro = LogicaVehiculo.asignar_mecanico('UEV109', '1234')
        
        self.assertTrue(resultado_registro)           