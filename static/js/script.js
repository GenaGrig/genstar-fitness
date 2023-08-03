function confirmDelete() {
    // Send an AJAX request to your Django view to delete the booking
    const id = 'appointment.id'; // Replace with the actual booking ID
    $.ajax({
        url: `delete_booking/<int:id>`, // Replace with your Django view URL
        type: 'DELETE',
        dataType: 'json',
        success: function(data) {
            redirect('userPanel.html'); // Replace with your Django view URL
        },
        error: function(error) {
            // Handle error
            console.log(error);
        }
    });
}