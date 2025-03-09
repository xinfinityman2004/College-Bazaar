// Initialize notification count
let currentCount = 4; // Set initial notification count to 4
const maxNotifications = 9; // Maximum notifications allowed
updateNotificationCount(currentCount); // Display 4 notifications in the bell icon

// Function to update the notification count in the bell icon
function updateNotificationCount(newCount) {
  document.getElementById('notificationCount').textContent = newCount;
}

// Toggle dropdown visibility when bell icon is clicked
document.getElementById('bellIcon').addEventListener('click', function() {
  const dropdown = document.getElementById('dropdownMenu');
  dropdown.classList.toggle('show');

  // Update the notification count when the dropdown is shown
  updateNotificationCount(currentCount); // Ensure the bell count reflects the number of notifications
});

// Simulate adding a new notification (you can replace this with actual event or condition)
setInterval(() => {
  if (currentCount < maxNotifications) { // Check if the count is less than the max allowed
    currentCount++; // Increase notification count by 1
    updateNotificationCount(currentCount); // Update the bell icon with the new count
    // Add a new notification to the dropdown (for demonstration purposes)
    addNewNotification(`New notification #${currentCount}`);
  }
}, 5000);

// Function to add a new notification to the dropdown
function addNewNotification(notificationText) {
  const dropdownList = document.querySelector('#dropdownMenu ul');
  
  // Create a new list item for the new notification
  const newNotification = document.createElement('li');
  newNotification.textContent = notificationText;
  
  // Append the new notification to the dropdown
  dropdownList.appendChild(newNotification);
}

// Clear all notifications when "Clear All" button is clicked
document.getElementById('clearAll').addEventListener('click', function() {
  currentCount = 0; // Reset notification count to 0
  updateNotificationCount(currentCount);  // Update the bell icon count
  document.getElementById('dropdownMenu').classList.remove('show');  // Hide the dropdown

  // Clear the dropdown list
  const dropdownList = document.querySelector('#dropdownMenu ul');
  dropdownList.innerHTML = ''; // Remove all notifications from the dropdown
});
