// You can replace this with your actual API call to Eventbrite or Meetup API
const events = [
    {
        title: "Cyberpunk Concert",
        description: "An electrifying cyberpunk concert with neon lights and techno music.",
        date: "2025-02-15",
        image: "https://via.placeholder.com/250"
    },
    {
        title: "Tech Conference 2025",
        description: "Join the latest trends and innovations in the tech industry.",
        date: "2025-03-01",
        image: "https://via.placeholder.com/250"
    },
    {
        title: "Music Festival 2025",
        description: "A 3-day music festival featuring the best artists from around the world.",
        date: "2025-04-10",
        image: "https://via.placeholder.com/250"
    }
];

// Function to render events
function displayEvents() {
    const eventList = document.getElementById("event-list");

    events.forEach(event => {
        const eventItem = document.createElement("div");
        eventItem.classList.add("event-item");

        eventItem.innerHTML = `
            <img src="${event.image}" alt="${event.title}">
            <h3>${event.title}</h3>
            <p>${event.description}</p>
            <p><strong>Date:</strong> ${event.date}</p>
        `;

        eventList.appendChild(eventItem);
    });
}

// Call the function to display events when the page loads
window.onload = displayEvents;
