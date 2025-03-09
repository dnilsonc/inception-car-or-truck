document.getElementById('imageInput').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    const preview = document.getElementById('imagePreview');
    
    reader.onload = (event) => {
        preview.innerHTML = `<img src="${event.target.result}" alt="Preview">`;
        preview.style.border = "none";
    };
    
    reader.readAsDataURL(file);
});

document.getElementById('analyzeButton').addEventListener('click', async function() {
    const fileInput = document.getElementById('imageInput');
    const file = fileInput.files[0];

    if (!file) {
        document.getElementById('result').textContent = "Por favor, carregue uma imagem primeiro!";
        return;
    }

    document.getElementById('result').innerHTML = '<div class="loading">Analisando...</div>';

    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('http://localhost:80/predict/', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            document.getElementById('result').innerHTML = `<div class="error">Erro: ${data.error}</div>`;
            return;
        }

        document.getElementById('result').innerHTML = `
            <div class="result-content">
                <span>Veículo identificado:</span>
                <strong>${data.prediction}</strong>
                <span>com ${(data.confidence * 100).toFixed(2)}% de confiança</span>
            </div>
        `;

    } catch (error) {
        document.getElementById('result').innerHTML = `<div class="error">Erro na conexão com a API</div>`;
        console.error('Error:', error);
    }
});
