document.addEventListener("DOMContentLoaded", function () {
    const conceptButton = document.querySelector(".concept-button");
    const stage1Button = document.querySelector(".stage-button:nth-child(2)");
    const stage2Button = document.querySelector(".stage-button:nth-child(3)");

    const conceptModal = document.getElementById("conceptModal");
    const stage1Modal = document.getElementById("stage1Modal");
    const stage2Modal = document.getElementById("stage2Modal");

    const closeModalButtons = document.querySelectorAll(".close");

    conceptButton.addEventListener("click", function () {
        conceptModal.style.display = "block";
    });

    stage1Button.addEventListener("click", function () {
        stage1Modal.style.display = "block";
    });

    stage2Button.addEventListener("click", function () {
        stage2Modal.style.display = "block";
    });

    closeModalButtons.forEach(function (closeButton) {
        closeButton.addEventListener("click", function () {
            conceptModal.style.display = "none";
            stage1Modal.style.display = "none";
            stage2Modal.style.display = "none";
        });
    });

    window.addEventListener("click", function (event) {
        if (event.target === conceptModal || event.target === stage1Modal || event.target === stage2Modal) {
            conceptModal.style.display = "none";
            stage1Modal.style.display = "none";
            stage2Modal.style.display = "none";
        }
    });

});
