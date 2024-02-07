function mostrarAngulo(valor){
    document.getElementById('outputAngulo').textContent = valor;
}

document.getElementById('angulo').addEventListener('change', function() {
    localStorage.setItem('angulo', this.value);
    localStorage.setItem('rango', this.value);
    document.getElementById('outputAngulo').textContent = this.value;
    document.getElementById('servoForm').submit();
});




