document.addEventListener("DOMContentLoaded", function() {
    const mensaje = document.getElementById('mensaje');

    if (enviado) {
        mensaje.style.display = 'block';
        setTimeout(() => {
            mensaje.style.display = 'none';
        }, 3000);
    }
});