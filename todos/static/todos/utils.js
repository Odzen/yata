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

    const observer = new MutationObserver(showOrHideEmptyMessage);

    observer.observe(targetNode, config);

    showOrHideEmptyMessage();
};