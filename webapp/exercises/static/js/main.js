document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("generateExercise").addEventListener("click", function() {
        document.getElementById("exerciseDisplay").textContent = "";
        document.getElementById("askForHint").style.display = "none";
        document.getElementById("hintDisplay").textContent = "";
        document.getElementById("generateExercise").style.display = "none";

        document.getElementById("spinner").style.display = "block";

        fetch("/get_random_exercise/")
            .then(response => response.json())
            .then(data => {
                setTimeout(() => {
                    document.getElementById("spinner").style.display = "none";

                    document.getElementById("exerciseDisplay").textContent = data.exercise;

                    document.getElementById("askForHint").style.display = "block";

                    document.getElementById("generateExercise").style.display = "block";
                }, 3000);
            })
            .catch(error => {
                document.getElementById("spinner").style.display = "none";
                document.getElementById("generateExercise").style.display = "block";

                console.error('There was an error fetching the exercise:', error);
            });
    });







    function convertUrlsToAnchors(text) {
    let urlPattern = /\bhttps?:\/\/\S+/gi;
    return text.replace(urlPattern, function(url) {
        return `<a href="${url}" target="_blank">${url}</a>`;
    });
}

    document.getElementById("askForHint").addEventListener("click", function() {
        let exerciseText = document.getElementById("exerciseDisplay").textContent;

        // Hide the "Get Hint" button to prevent multiple clicks
        document.getElementById("askForHint").style.display = "none";

        // Show the spinner
        document.getElementById("spinner").style.display = "block";

        fetch(`/get_hint_from_chatgpt/?exercise=${encodeURIComponent(exerciseText)}`)
            .then(response => {
                return response.json();
            })
            .then(data => {
                // Hide the spinner
                document.getElementById("spinner").style.display = "none";

                console.log("Data Received:", data);
                let hintDisplay = document.getElementById("hintDisplay");
                if (data.hint) {
                    hintDisplay.innerHTML = convertUrlsToAnchors("" + data.hint);
                } else if (data.error) {
                    hintDisplay.textContent = "Error: " + data.error;
                }
            })
            .catch(error => {
                // Hide the spinner
                document.getElementById("spinner").style.display = "none";

                console.error('There was an error fetching the hint:', error);
                document.getElementById("hintDisplay").textContent = "Error fetching hint!";
            });
    });

});