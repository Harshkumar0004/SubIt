const videoInput = document.getElementById("videoInput");
const videoPlayer = document.getElementById("videoPlayer");
const videoBox = document.getElementById("videoBox");
const generateBtn = document.getElementById("generateBtn");
const downloadLink = document.getElementById("downloadLink");

videoInput.addEventListener("change", function () {
  const file = videoInput.files[0];
  if (file) {
    const videoURL = URL.createObjectURL(file);
    videoPlayer.src = videoURL;
    videoBox.style.display = "none";
    videoPlayer.style.display = "block";
  }
});

generateBtn.addEventListener("click", async function () {
  const file = videoInput.files[0];
  if (!file) {
    alert("Please upload a video first.");
    return;
  }

  const formData = new FormData();
  formData.append("video", file);

  generateBtn.textContent = "⏳ Generating...";
  generateBtn.disabled = true;

  try {
    const response = await fetch("/generate", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      alert("Failed to generate subtitles.");
      return;
    }

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);

    downloadLink.href = url;
    downloadLink.style.display = "inline";
  } catch (error) {
    console.error("Error:", error);
    alert("An error occurred while generating subtitles.");
  } finally {
    generateBtn.textContent = "🎤 Generate Subtitles";
    generateBtn.disabled = false;
  }
});
