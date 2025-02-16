async function getAllUsers() {
  let response = await fetch('/api/users');
  let users = await response.json();
  updateTable(users);
}

async function getLatestUser() {
  let response = await fetch('/api/users?latest=true');
  let latestUser = await response.json();
  updateTable([latestUser]);
}

async function clearOutput() {
  document.querySelector("#usersTable tbody").innerHTML = "";
  return document.querySelector("#usersTable tbody");
}

/**
 * Updates the table with user data.
 * @param {Array} users - List of users to display.
 */
function updateTable(users) {
  let tableBody = clearOutput();

  if (users.length === 0) {
    tableBody.innerHTML = "<tr><td colspan='3'>No users found.</td></tr>";
    return;
  }

  users.forEach(user => {
    let row = document.createElement("tr");
    row.innerHTML = `
          <td>${user.name}</td>
          <td>${user.country}</td>
          <td>${user.cat_amount}</td>
      `;
    tableBody.appendChild(row);
  });
}


document.getElementById("userForm").addEventListener("submit", async function (event) {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const country = document.getElementById("country").value;
  const catAmount = document.getElementById("cat_amount").value;

  const userData = {
    name: name,
    country: country,
    cat_amount: parseInt(catAmount)
  };

  try {
    let response = await fetch('/api/users', {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(userData)
    });

    let data = await response.json();
    document.getElementById("message").innerText = data.message;

    document.getElementById("userForm").reset();
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("message").innerText = "Error adding user.";
  }
});
