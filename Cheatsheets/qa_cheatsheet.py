## SDET Cheatsheet - Pruebas Automatizadas con Python ##

## Frameworks de Pruebas ##
import unittest
import pytest

## Configuración y Limpieza ##
def setUp():
    # Configuración inicial antes de cada prueba

def tearDown():
    # Limpieza después de cada prueba

## Asserts y Verificaciones ##
# Unittest
self.assertEqual(a, b)          # Verifica que a y b sean iguales
self.assertNotEqual(a, b)       # Verifica que a y b no sean iguales
self.assertTrue(x)              # Verifica que x sea verdadero
self.assertFalse(x)             # Verifica que x sea falso
self.assertIs(a, b)             # Verifica que a y b sean el mismo objeto
self.assertIsNot(a, b)          # Verifica que a y b no sean el mismo objeto
self.assertIn(a, b)             # Verifica que a esté en b
self.assertNotIn(a, b)          # Verifica que a no esté en b
self.assertRaises(Error, func)  # Verifica que func genere una excepción de tipo Error

# Pytest
assert a == b                   # Verifica que a y b sean iguales
assert a != b                   # Verifica que a y b no sean iguales
assert x                        # Verifica que x sea verdadero
assert not x                    # Verifica que x sea falso
assert a is b                   # Verifica que a y b sean el mismo objeto
assert a is not b               # Verifica que a y b no sean el mismo objeto
assert a in b                   # Verifica que a esté en b
assert a not in b               # Verifica que a no esté en b
with pytest.raises(Error):      # Verifica que la función genere una excepción de tipo Error
    func()

## Ejecución de Pruebas ##
# Unittest
if __name__ == '__main__':
    unittest.main()

# Pytest
# Ejecutar todas las pruebas en el directorio actual
pytest

# Ejecutar pruebas en un archivo específico
pytest test_file.py

# Ejecutar solo una prueba específica por nombre
pytest -k test_name

# Generar reporte HTML
pytest --html=report.html

## Selenium WebDriver ##
# Instalación
pip install selenium

# Importar WebDriver
from selenium import webdriver

# Configuración básica
driver = webdriver.Firefox()          # Crear una instancia del driver
driver.get("https://www.example.com") # Navegar a una URL

# Localizar elementos
element = driver.find_element_by_id("element_id")          # Localizar elemento por ID
element = driver.find_element_by_name("element_name")      # Localizar elemento por nombre
element = driver.find_element_by_xpath("xpath_expression") # Localizar elemento por XPath
element = driver.find_element_by_css_selector("css_selector") # Localizar elemento por selector CSS

# Interactuar con elementos
element.click()                    # Hacer clic en un elemento
element.send_keys("text")          # Escribir texto en un campo de entrada
element.clear()                    # Borrar el contenido de un campo de entrada
element.get_attribute("attribute") # Obtener el valor de un atributo de un elemento

# Esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id")))

# Cerrar el driver
driver.quit()
