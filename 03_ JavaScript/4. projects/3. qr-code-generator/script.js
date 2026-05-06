document.querySelector("#generateBtn").addEventListener("click", handleQrCodeGeneration);

function handleQrCodeGeneration() {
    const inputText = document.querySelector("#input").value;
    if (!inputText) {
        alert("Please enter some text to generate a QR code.");
        return;
    }
    const code = document.querySelector("#code");
    new QRious({
        element: code,
        value: inputText,
    });
    code.style.display = "block";
}
    
