const profileData = {
  name: "Juan Dela Cruz",
  role: "Musician",
  location: "Cebu City",
  email: "juandelacruz@gmail.com",
  instruments: "Guitar, Piano",
  genres: "Jazz, Pop",
}

function toggleEdit() {
  loadEditForm()
  document.getElementById("viewMode").classList.add("hidden")
  document.getElementById("editMode").classList.remove("hidden")
}

function cancelEdit() {
  document.getElementById("editMode").classList.add("hidden")
  document.getElementById("viewMode").classList.remove("hidden")
}

function loadEditForm() {
  document.getElementById("editFullName").value = profileData.name
  document.getElementById("editEmail").value = profileData.email
  document.getElementById("editRole").value = profileData.role
  document.getElementById("editInstruments").value = profileData.instruments
  document.getElementById("editGenres").value = profileData.genres
  document.getElementById("editLocation").value = profileData.location
  document.getElementById("editNameHeader").value = profileData.name
  document.getElementById("editRoleHeader").value = profileData.role
  document.getElementById("editLocationHeader").value = profileData.location
}

function saveProfile() {
  profileData.name = document.getElementById("editFullName").value
  profileData.email = document.getElementById("editEmail").value
  profileData.role = document.getElementById("editRole").value
  profileData.instruments = document.getElementById("editInstruments").value
  profileData.genres = document.getElementById("editGenres").value
  profileData.location = document.getElementById("editLocation").value

  updateViewDisplay()
  cancelEdit()
}

function updateViewDisplay() {
  document.getElementById("viewName").textContent = profileData.name
  document.getElementById("viewRole").textContent = profileData.role
  document.getElementById("viewLocation").textContent = profileData.location
  document.getElementById("viewFullName").textContent = profileData.name
  document.getElementById("viewEmail").textContent = profileData.email
  document.getElementById("viewRoleField").textContent = profileData.role
  document.getElementById("viewInstruments").textContent = profileData.instruments
  document.getElementById("viewGenres").textContent = profileData.genres
  document.getElementById("viewLocationField").textContent = profileData.location
}

// Initialize view on page load
document.addEventListener("DOMContentLoaded", () => {
  updateViewDisplay()
  document.getElementById("viewMode").classList.remove("hidden")
})
