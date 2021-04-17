class Table {
    constructor(rootElement) {
        this.rootElement = rootElement;
        this.columns = [];
        this.data = [];
        this.index = [];
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

    render() {
        if (this.rootElement == null) {
            return;
        }

        const table = $(this.rootElement).find("table");
        table.empty();

        const thead = $("<thead>").append(this.buildRow("#", this.columns, true));
        table.append(thead);

        const tbody = $("<tbody>");
        for (let i = 0; i < this.index.length; ++i) {
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
}