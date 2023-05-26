  // Predefined questions and answers
  const faq = [
    { question: "hai", answer: "Hai How can i help you ?" },
    { question: "hello", answer: "Hai How can i help you ?" },
    { question: "hi", answer: "Hai How can i help you ?" },
    { question: "goodbye", answer: "Talk to you later!" },
    { question: "nice talking to you!", answer: "I am glad I could help" },
    { question: "internship", answer: "We are providing internships for Python,React,Digital marketing ,Machine learning." },
    { question: "what internship", answer: "We are providing internships for Python,React,Digital marketing ,Machine learning." },
    { question: "what internship?", answer: "We are providing internships for Python,React,Digital marketing ,Machine learning." },
    { question: "wfh", answer: "Currently we are providing Work from home" },
    { question: "work from home", answer: "Currently we are providing Work from home" },
    { question: "are you sure that i will get job in this company itself?", answer: "Yes,you will get job confirmation offer letter within 2 days of your joining." },
    { question: "is this work from home or work from office?", answer: "is this work from home or work from office?" },
    { question: "will i ever have to come the office for work?", answer: "According to our rules and regulations if any time relocation is available you have to accept it." },
    { question: "Is there any bond in your company ?", answer: "No" },
    { question: "What about the salary package?", answer: "12k to 18k" },
    { question: "What about the working hours?", answer: "8 hours" },
    { question: "Other than python in which other streams do you provide internships?", answer: "For React,Digital marketing ,Machine learning." },
    { question: "How can I apply for this?", answer: "Please contact to our HR , tel: +91 9074 156 818 " },

    
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
      displayMessage("Q: "+ question); // Display user question

      // Search for a matching question in the faq array
      const matchingQuestion = faq.find((entry) => entry.question.toLowerCase() === question.toLowerCase());
      if (matchingQuestion) {
        displayMessage("Ans: "+ matchingQuestion.answer); // Display the corresponding answer
      } else {
        displayMessage("Please contact to our HR  for more details, tel: +91 9074 156 818 "); // Display default response
      }
    }
  });