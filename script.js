// Assume you have a function that retrieves the message from the AI model
function getMessageFromAIModel() {
    // For demonstration purposes, let's assume the message is hardcoded
    return "Obstacle detected ahead. Please proceed with caution.";
}

// Function to display the message on the webpage
function displayMessage() {
    const messageContainer = document.getElementById("message-container");
    const message = getMessageFromAIModel();
    messageContainer.innerHTML = `<p>${message}</p>`;
}

// Call the displayMessage function when the page loads
window.onload = function() {
    displayMessage();
};
