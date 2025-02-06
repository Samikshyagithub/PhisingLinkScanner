async function scanUrl() {
  const url = document.getElementById("urlInput").value;
  const resultDiv = document.getElementById("result");

  if (!url) {
    resultDiv.innerText = "Please enter a URL.";
    return;
  }

  try {
    const response = await fetch(
      `http://localhost:5000/scan?url=${encodeURIComponent(url)}`
    );
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const result = await response.json();

    if (result.error) {
      resultDiv.innerText = result.error;
    } else {
      resultDiv.innerText = `${result.message} (Confidence: ${(
        result.confidence * 100
      ).toFixed(2)}%)`;
    }
  } catch (error) {
    console.error("Error:", error);
    resultDiv.innerText = "An error occurred. Please try again.";
  }
}
