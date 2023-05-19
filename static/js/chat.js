  // Predefined questions and answers
  const faq = [
    { question: "What is your name?", answer: "My name is ChatBot." },
    { question: "What can you do?", answer: "I can answer frequently asked questions." },
    // Add more question-answer pairs here
  ];

  // Get necessary DOM elements
  const userInput = document.getElementById("user-input");
  const sendBtn = document.getElementById("send-btn");
  const chatMessages = document.getElementById("chat-messages");
  var isUserMessage = true

  // Function to display a message in the chat box
  function displayMessage(message) {
    const messageElement = document.createElement("div");
    messageElement.className = "message";
    messageElement.textContent = message;

    if (isUserMessage) {
      messageElement.classList.add("user-message");
      isUserMessage = false
     
    } else {
      messageElement.classList.add("bot-message");
      isUserMessage = true
     
    }
    
    chatMessages.appendChild(messageElement);
    
    
  }

  // Event listener for send button click
  sendBtn.addEventListener("click", function () {
    const question = userInput.value.trim();
    userInput.value = ""; // Clear the input field

    if (question !== "") {
      displayMessage(question); // Display user question

      // Search for a matching question in the faq array
      const matchingQuestion = faq.find((entry) => entry.question.toLowerCase() === question.toLowerCase());
      if (matchingQuestion) {
        displayMessage(matchingQuestion.answer); // Display the corresponding answer
      } else {
        displayMessage("Sorry, ."); // Display default response
      }
    }
  });