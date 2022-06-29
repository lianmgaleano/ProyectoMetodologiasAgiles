import unittest
from logica.logicaVehiculo import LogicaVehiculo

class test_ingresar_vehiculo (unittest.TestCase) :
    
    def test_ingresar_vehiculo (self):
        """Prueba de registro de un vehículo"""
        resultado_registro = LogicaVehiculo.registrar_vehiculo('UEV100', 'buseta', '654321987')
        
        self.assertTrue(resultado_registro)
        
    def test_ingresar_vehiculo_existente (self):
        """Prueba de registro de un vehículo existente"""
        resultado_registro = LogicaVehiculo.registrar_vehiculo('UEV100', 'buseta', '654321987')    
        
        self.assertTrue(resultado_registro)
        