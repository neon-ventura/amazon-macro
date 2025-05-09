import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

def abrir_amazon_fashion():
    # Abre o navegador Chrome
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com.br/s?i=fashion&srs=206761987011&bbn=206761987011&rh=n%3A17365811011%2Cp_85%3A19171728011&dc&pf_rd_i=17365811011&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_s=merchandised-search-5_CW&qid=1746735943&rnid=19171727011&xpid=wbQkZUbc0p62K&ref=sr_pg_1")
    return driver

def encontrar_produtos(driver):
    # Lista de diferentes seletores para tentar encontrar os produtos
    selectors = [
        "div.s-image-padding",
        "div[data-component-type='s-search-result']",
        "div.s-result-item",
        "div.a-section.a-spacing-base",
        "div.sg-col-inner"
    ]
    
    for selector in selectors:
        try:
            produtos = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
            )
            if len(produtos) > 0:
                print(f"Produtos encontrados usando o seletor: {selector}")
                return produtos
        except:
            continue
    
    return None

def clicar_produto(driver, produto):
    # Tenta diferentes métodos de clique
    try:
        # Método 1: Clique direto
        produto.click()
        return True
    except:
        try:
            # Método 2: Clique via JavaScript
            driver.execute_script("arguments[0].click();", produto)
            return True
        except:
            try:
                # Método 3: Clique via ActionChains
                ActionChains(driver).move_to_element(produto).click().perform()
                return True
            except:
                try:
                    # Método 4: Clique via coordenadas
                    location = produto.location
                    size = produto.size
                    x = location['x'] + size['width']/2
                    y = location['y'] + size['height']/2
                    pyautogui.click(x, y)
                    return True
                except:
                    return False

def clicar_produto_especifico(driver, indice=0):
    try:
        # Aguarda a página carregar completamente
        time.sleep(3)
        
        # Tenta encontrar os produtos usando diferentes métodos
        produtos = encontrar_produtos(driver)
        
        if produtos and len(produtos) > indice:
            # Rola até o elemento para garantir que está visível
            driver.execute_script("arguments[0].scrollIntoView(true);", produtos[indice])
            time.sleep(1)
            
            # Tenta clicar no produto usando diferentes métodos
            if clicar_produto(driver, produtos[indice]):
                print(f"Produto {indice + 1} clicado com sucesso!")
                
                # Aguarda 3 segundos na página do produto
                time.sleep(3)
                
                # Volta para a página de moda
                driver.get("https://www.amazon.com.br/s?i=fashion&srs=206761987011&bbn=206761987011&rh=n%3A17365811011%2Cp_85%3A19171728011&dc&pf_rd_i=17365811011&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_s=merchandised-search-5_CW&qid=1746735943&rnid=19171727011&xpid=wbQkZUbc0p62K&ref=sr_pg_1")
                print("Retornou para a página de moda!")
            else:
                print(f"Não foi possível clicar no produto {indice + 1}")
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

    # Inicia o navegador e abre a página de moda
    driver = abrir_amazon_fashion()
    
    # Clica nos 13 primeiros produtos
    for i in range(13):
        clicar_produto_especifico(driver, i)
        time.sleep(2)  # Aguarda entre cada clique
    
    # Mantém o navegador aberto
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    main() 