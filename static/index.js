

document.getElementById('velocidad').addEventListener('input', function () {
    // Guardar el valor en el almacenamiento local
    localStorage.setItem('velocidad', this.value);
    localStorage.setItem('rango', this.value);
    document.getElementById('outputVelocidad').textContent = this.value;
    document.getElementById('motorForm').submit();
});


function mostrarValorMotor(valor){
    document.getElementById('outputVelocidad').textContent = valor;
}









