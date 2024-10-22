
class MultipleSelectComponent {
    listSelector = ".multiple-select-list";
    addBtnSelector = ".multiple-select-add";
    selectedListSelector = ".multiple-select-div";

    constructor(rootSelector) {
        console.log("MultipleSelectComponent: ", rootSelector)
        this.rootElement = document.querySelector(rootSelector);
        if (this.rootElement) {
            this.list = this.rootElement.querySelector(this.listSelector);
            this.addBtn = this.rootElement.querySelector(this.addBtnSelector);
            this.selectedList = this.rootElement.querySelector(this.selectedListSelector);
            this.addListeners();
        } else {
            console.error("MultipleSelectComponent: Could not find root element with selector", this.listSelector);
        }
    }

    addSelectOption(text, value){
        let option = document.createElement('div');
        option.textContent = text;
        option.dataset.value = value;
        this.selectedList.appendChild(option);
    }

    addListeners(){
        // Select option
        this.addBtn.addEventListener('click', () => {
            var selected = this.list.options[this.list.selectedIndex];
            if (selected) {
                var existingOption = Array.from(this.list.children).find(option => option.dataset.value === selected.value);
                if (!existingOption) {
                    selected.disabled = true;
                    selected.selected = false;
                    this.addSelectOption(selected.text, selected.value);
                }
            }
        });
        // Delete for click on selected option
        this.selectedList.addEventListener('click', (event) => {
            if (event.target.tagName === 'DIV' && this.selectedList != event.target) {
                var option = this.list.querySelector(`option[value="${event.target.dataset.value}"]`);
                if (option) {
                    option.disabled = false;
                }
                event.target.remove();
            }
        });
        // 
    }
}
