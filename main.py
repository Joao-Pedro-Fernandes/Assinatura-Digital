from pyhanko.sign import signers
from pyhanko.sign.fields import SigFieldSpec
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter

pdf_entrada = str(input("Digite o nome do arquivo com a extensão .pdf:"))
certificado_pfx = str(input("Digite o nome do arquivo de certificado .pfx:"))
senha_certificado = str(input("Digite a senha do certificado:"))
pdf_saida = "documento_assinado.pdf"

assinador = signers.SimpleSigner.load_pkcs12(certificado_pfx,senha_certificado.encode("utf-8"))


pdf_signer = signers.PdfSigner(
    signers.PdfSignatureMetadata(field_name="Assinatura"),
    signer=assinador,
    new_field_spec=SigFieldSpec(sig_field_name="Assinatura")
)

with open(pdf_entrada, "rb") as document_in, open(pdf_saida, "wb") as document_out:
    writer = IncrementalPdfFileWriter(document_in)
    pdf_signer.sign_pdf(writer, output=document_out)

print("PDF assinado com sucesso!") 