function showOrHideEmptyMessage() {

    const itemCount = Array.from(document.getElementsByClassName("todo_item")).length;

    if (itemCount === 0) {
        document.getElementById("todo_items_empty").style.display = "block";
    } else {
        document.getElementById("todo_items_empty").style.display = "none";
    }
}

window.onload = function () {
    const targetNode = document.getElementById("todo_items");

    const config = {
        childList: true,
    };

    const observer = new MutationObserver(showOrHideEmptyMessage);s

    observer.observe(targetNode, config);
};

document.addEventListener("htmx:afterRequest", function(event) {
    if (event.detail.verb === "post") {
        document.getElementById("create-form").reset();
    }
});