# Assinador de PDF com PyHanko

Este projeto permite assinar digitalmente arquivos PDF utilizando certificados no formato **.pfx**. Ele utiliza a biblioteca **PyHanko**, que fornece funcionalidades para assinatura digital baseada em criptografia assimétrica.

---

## Requisitos

- Python 3.10 ou superior
- Biblioteca PyHanko

Instale a biblioteca necessária com:

```bash
pip install pyhanko
´´´

Funcionalidades

Assina arquivos PDF usando certificados digitais (.pfx).

Cria uma assinatura digital incorporada no PDF.

Garante a integridade e autenticidade do documento.

Como usar

Clone ou baixe este repositório.

Prepare um arquivo PDF que deseja assinar.

Tenha em mãos um certificado digital .pfx e a senha correspondente.

Execute o script:

python assinar_pdf.py


O programa solicitará:

Digite o nome do arquivo com a extensão .pdf: 
Digite o nome do arquivo de certificado .pfx: 
Digite a senha do certificado: 


Após a execução, o PDF assinado será salvo como documento_assinado.pdf.
