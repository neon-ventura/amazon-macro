import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def abrir_amazon_bestsellers():
    # Abre o navegador Chrome
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com.br/gp/bestsellers")
    return driver

def clicar_produto_especifico(driver, indice=0):
    try:
        # Aguarda a página carregar completamente
        time.sleep(3)
        
        # Tenta encontrar todos os elementos com a classe específica
        produtos = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-section.a-spacing-mini._cDEzb_noop_3Xbw5"))
        )
        
        if len(produtos) > indice:
            # Rola até o elemento para garantir que está visível
            driver.execute_script("arguments[0].scrollIntoView(true);", produtos[indice])
            time.sleep(1)
            
            # Tenta clicar usando JavaScript
            driver.execute_script("arguments[0].click();", produtos[indice])
            print(f"Produto {indice + 1} clicado com sucesso!")
            
            # Aguarda um pouco após clicar no produto
            time.sleep(2)
            
            # Volta para a página de mais vendidos
            driver.get("https://www.amazon.com.br/gp/bestsellers")
            print("Retornou para a página de mais vendidos!")
        else:
            print(f"Não foi possível encontrar o produto {indice + 1}")
            
    except TimeoutException:
        print("Tempo esgotado ao procurar o elemento")
    except NoSuchElementException:
        print("Elemento não encontrado na página")
    except Exception as e:
        print(f"Erro ao interagir com o elemento: {str(e)}")

def main():
    # Configurações do PyAutoGUI
    pyautogui.PAUSE = 1.5  # Pausa entre ações
    pyautogui.FAILSAFE = True  # Mova o mouse para o canto superior esquerdo para parar o script

    # Inicia o navegador e abre a página de mais vendidos
    driver = abrir_amazon_bestsellers()
    
    # Clica no primeiro produto
    clicar_produto_especifico(driver, 0)
    
    # Aguarda um pouco antes de clicar no segundo produto
    time.sleep(3)
    
    # Clica no segundo produto
    clicar_produto_especifico(driver, 1)
    
    # Aguarda um pouco antes de clicar no terceiro produto
    time.sleep(3)
    
    # Clica no terceiro produto
    clicar_produto_especifico(driver, 2)
    
    # Mantém o navegador aberto
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    main() 