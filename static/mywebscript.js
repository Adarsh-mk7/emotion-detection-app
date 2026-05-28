let RunSentimentAnalysis = () => {
  let textToAnalyze = document.getElementById("textToAnalyze").value;

  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4) {
      let displayDiv = document.getElementById("system_response");

      // Make the response container visible on the webpage
      displayDiv.style.display = "block";

      if (this.status == 200) {
        displayDiv.innerHTML = xhttp.responseText;
      } else {
        displayDiv.innerHTML =
          "<span class='text-danger'>Error: Could not reach the server. Check backend console logs.</span>";
      }
    }
  };

  // FIXED: Added leading '/' to target the absolute path correctly
  xhttp.open(
    "GET",
    "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
    true,
  );
  xhttp.send();
};
