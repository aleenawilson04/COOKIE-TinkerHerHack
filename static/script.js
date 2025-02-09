document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const location = document.getElementById('location').value;
    fetchEvents(location);
});

function fetchEvents(location) {
    fetch(`/events?location=${encodeURIComponent(location)}`)
        .then(response => response.json())
        .then(data => {
            displayEvents(data);
        })
        .catch(error => console.error('Error fetching events:', error));
}

function displayEvents(events) {
    const eventList = document.getElementById('event-list');
    eventList.innerHTML = ''; // Clear previous events

    if (events.length === 0) {
        eventList.innerHTML = '<p>No events found.</p>';
        return;
    }

    events.forEach(event => {
        const eventItem = document.createElement('div');
        eventItem.classList.add('event-item');

        const eventImage = event.logo ? event.logo.url : 'https://via.placeholder.com/250';
        const eventName = event.name.text;
        const eventDescription = event.description.text;
        const eventDate = event.start.local;
        const eventVenue = event.venue ? event.venue.name : 'Venue not specified';

        eventItem.innerHTML = `
            <img src="${eventImage}" alt="${eventName}">
            <h3>${eventName}</h3>
            <p>${eventDescription}</p>
            <p><strong>Date:</strong> ${eventDate}</p>
            <p><strong>Venue:</strong> ${eventVenue}</p>
        `;

        eventList.appendChild(eventItem);
    });
}