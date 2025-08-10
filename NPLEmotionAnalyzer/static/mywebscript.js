let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
            if (this.status === 200) {
                try {
                    const response = JSON.parse(this.responseText);
                    const dominant = response.dominant_emotion;

                    const emotions = Object.entries(response)
                        .filter(([k]) => k !== "dominant_emotion")
                        .sort((a, b) => b[1] - a[1]);

                    const tableBody = document.getElementById("emotionTableBody");
                    tableBody.innerHTML = "";

                    for (const [emotion, value] of emotions) {
                        const isDominant = emotion === dominant;
                        const row = `
                            <tr class="${isDominant ? 'table-success' : ''}">
                                <td><strong>${emotion}</strong></td>
                                <td>${(value * 100).toFixed(2)}%</td>
                            </tr>`;
                        tableBody.innerHTML += row;
                    }

                    document.getElementById("system_response").innerHTML = `
                        <p><strong>Dominant Emotion:</strong> ${dominant}</p>
                    `;
                } catch (error) {
                    document.getElementById("system_response").innerHTML = "Error parsing response.";
                    console.error("Parsing error:", error);
                }
            } else if (this.status === 400) {
                alert("¡Texto inválido! ¡Por favor, inténtalo de nuevo!");
                document.getElementById("emotionTableBody").innerHTML = "";
                document.getElementById("system_response").innerHTML = "";
            }
        }
    };

    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
