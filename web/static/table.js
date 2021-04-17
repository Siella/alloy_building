class Table {
    constructor(rootElement) {
        this.rootElement = rootElement;
        this.columns = [];
        this.data = [];
        this.index = [];
        this.targets = [];
        this.maxRows = 100;
        this.render();
    }

    loadData(data) {
        this.columns = data.columns;
        this.data = data.data;
        this.index = data.index;
        this.render();
    }

    buildRow(index, cols, isHead) {
        const tr = $("<tr>");
        tr.append($("<th>").attr("scope", isHead ? "col" : "row").text(index));

        for (const col of cols) {
            tr.append(
                (isHead ? $("<th>").attr("scope", "col") : $("<td>")).text(col)
            );
        }

        return tr;
    }

    hide() {
        $(this.rootElement).hide();
    }

    show() {
        $(this.rootElement).show();
    }

    hideTable() {
        $(this.rootElement).find("table").hide();
    }

    showTable() {
        $(this.rootElement).find("table").show();
    }

    hideWaiting() {
        $(this.rootElement).find(".goose-loading-indicator").hide();
    }

    showWaiting() {
        $(this.rootElement).find(".goose-loading-indicator").show();
    }

    render() {
        if (this.rootElement == null) {
            return;
        }

        const table = $(this.rootElement).find("table");
        table.empty();

        const thead = $("<thead>").append(this.buildRow("#", this.columns, true));
        table.append(thead);

        const tbody = $("<tbody>");
        for (let i = 0; i < this.index.length && i < this.maxRows; ++i) {
            tbody.append(this.buildRow(this.index[i], this.data[i], false));
        }
        table.append(tbody);
    }

    column(name) {
        const index = this.columns.indexOf(name);
        if (index < 0) {
            return undefined;
        }
        return this.data.map(item => item[index]);
    }

    exportAsCsv() {
        const head = "#," + this.columns.join(",");
        const body = [];
        for (let i = 0; i < this.index.length; ++i) {
            body.push(this.index[i] + "," + this.data[i].join(","));
        }

        return head + "\n" + body.join("\n");
    }

    filterColumns(cols) {
        const indices = [];
        for (const col of cols) {
            const index = this.columns.indexOf(col);
            if (index >= 0) {
                indices.push(index);
            }
        }

        const result = new Table(null);
        result.loadData({
            columns: indices.map(idx => this.columns[idx]),
            index: this.index,
            data: this.data.map(row => indices.map(idx => row[idx]))
        });

        return result;
    }
}