document.addEventListener("DOMContentLoaded", function() {
    function actualizarFechaHora() {
        // Obtener la etiqueta por su ID
        var etiqueta = document.getElementById("dato");

        // Hacer una solicitud al servidor para obtener la fecha y hora actualizadas
        fetch('/controlar_sensor')
            .then(response => response.text())
            .then(data => {
                // Actualizar el contenido de la etiqueta con la fecha y hora obtenidas del servidor
                etiqueta.innerHTML = data; // Cambiado a 'innerHTML'
            })
            .catch(error => console.error('Error:', error));
    }

    // Llamar a la función inicialmente
    actualizarFechaHora();

    // Llamar a la función cada segundo (1000 milisegundos)
    setInterval(actualizarFechaHora, 1000);
});
