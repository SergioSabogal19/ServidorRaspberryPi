document.addEventListener("DOMContentLoaded", function() {
    function actualizarTemp() {
        
        var etiqueta = document.getElementById("temp");

        // Hacer una solicitud al servidor para obtener la fecha y hora actualizadas
        fetch('/controlar_temp')
            .then(response => response.text())
            .then(data => {
                // Actualizar el contenido de la etiqueta con la fecha y hora obtenidas del servidor
                etiqueta.innerHTML = data; // Cambiado a 'innerHTML'
            })
            .catch(error => console.error('Error:', error));
    }

    // Llamar a la función inicialmente
    actualizarTemp();

    // Llamar a la función cada segundo (1000 milisegundos)
    setInterval(actualizarTemp, 1000);
});
