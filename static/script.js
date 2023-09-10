$(document).ready(function() {
    refreshList();

    // Refresh the list every 10 seconds
    setInterval(refreshList, 10000);
});

function refreshList() {
    $.getJSON("/list_inactive_vms", function(data) {
        $("#inactive-list").empty();
        data.forEach(function(vm) {
            $("#inactive-list").append('<li class="list-group-item">' + vm + '<button class="btn btn-success btn-sm" onclick="startVM(\'' + vm + '\')">Start</button></li>');
        });
    });

    $.getJSON("/list_active_vms", function(data) {
        $("#active-list").empty();
        data.forEach(function(vm) {
            $("#active-list").append('<li class="list-group-item">' + vm + '<button class="btn btn-danger btn-sm" onclick="stopVM(\'' + vm + '\')">Stop</button></li>');
        });
    });
}

function startVM(vmName) {
    $.post("/start_vm", { vm_name: vmName }, function() {
        refreshList();
    });
}

function stopVM(vmName) {
    $.post("/stop_vm", { vm_name: vmName }, function() {
        refreshList();
    });
}
