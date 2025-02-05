async function scanUrl() {
  const url = document.getElementById("urlInput").value;
  try {
    const response = await fetch(
      `http://localhost:5000/scan?url=${encodeURIComponent(url)}`
    );
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const result = await response.json();
    document.getElementById("result").innerText = result.message;
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("result").innerText =
      "An error occurred. Please try again.";
  }
}
