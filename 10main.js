document.getElementById('form-workshop').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Simulação de envio de formulário
    const btn = document.querySelector('.btn-submit');
    const msg = document.getElementById('msg-sucesso');
    
    btn.disabled = true;
    btn.innerText = 'A processar...';
    
    setTimeout(() => {
        btn.style.display = 'none';
        msg.style.display = 'block';
    }, 1500);
});

// Scroll suave para o botão principal
document.querySelector('.btn-main').addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    target.scrollIntoView({ behavior: 'smooth' });
});