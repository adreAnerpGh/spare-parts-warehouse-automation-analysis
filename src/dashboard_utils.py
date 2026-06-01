try:
    from IPython.display import HTML
except ImportError:
    HTML = None


STATUS_COLOURS = {
    "Green": "#2e7d32",
    "Amber": "#f9a825",
    "Red": "#c62828"
}


def _check_html():

    if HTML is None:
        raise ImportError(
            "dashboard_utils requires Jupyter/IPython "
            "to render HTML dashboards."
        )


def _status_circle(status):

    colour = STATUS_COLOURS.get(
        status,
        "#757575"
    )

    return f"""
    <span style="
        display:inline-block;
        width:22px;
        height:22px;
        border-radius:50%;
        background:{colour};
    ">
    </span>
    """


def render_kpi_board(
    title,
    kpi_df,
    return_html=False
):
    """
    Required columns:

    KPI
    Value
    """

    _check_html()

    cards = ""

    for _, row in kpi_df.iterrows():

        cards += f"""
        <div style="
            flex:1;
            min-width:180px;
            margin:10px;
            padding:20px;
            background:#1b1f2a;
            border-radius:10px;
            border:1px solid #30363d;
            text-align:center;
        ">

            <div style="
                color:#9aa4b2;
                font-size:14px;
            ">
                {row['KPI']}
            </div>

            <div style="
                color:white;
                font-size:28px;
                font-weight:bold;
                margin-top:10px;
            ">
                {row['Value']}
            </div>

        </div>
        """

    html = f"""
    <div style="
        font-family:Segoe UI;
        background:#0f1117;
        padding:20px;
        border-radius:10px;
    ">

        <h2 style="
            color:white;
            margin-bottom:20px;
        ">
            {title}
        </h2>

        <div style="
            display:flex;
            flex-wrap:wrap;
        ">

            {cards}

        </div>

    </div>
    """

    if return_html:
        return html

    return HTML(html)


def render_control_tower(
    title,
    dashboard_df,
    actions=None,
    legend=None,
    return_html=False
):
    """
    Required columns:

    Control
    Status
    Operational_Reading
    """

    _check_html()

    rows = ""

    for _, row in dashboard_df.iterrows():

        rows += f"""
        <tr style="
            border-bottom:1px solid #30363d;
        ">

            <td style="
                padding:12px;
                color:white;
            ">
                {row['Control']}
            </td>

            <td style="
                padding:12px;
                text-align:center;
            ">
                {_status_circle(row['Status'])}
            </td>

            <td style="
                padding:12px;
                color:#d6d6d6;
            ">
                {row['Operational_Reading']}
            </td>

        </tr>
        """

    action_html = ""

    if actions:

        action_html += """
        <div style="
            margin-top:25px;
            background:#1b1f2a;
            padding:15px;
            border-radius:10px;
            border:1px solid #30363d;
        ">

        <h3 style="
            color:white;
            margin-top:0px;
        ">
            Recommended Actions
        </h3>

        <ul style="
            color:#d6d6d6;
        ">
        """

        for action in actions:

            action_html += f"""
            <li style="margin-bottom:8px;">
                {action}
            </li>
            """

        action_html += """
        </ul>
        </div>
        """

    # -------------------------
    # LEGEND BLOCK
    # -------------------------

    legend_html = ""

    if legend:

        legend_html += """
        <div style="
            margin-top:20px;
            background:#161b22;
            padding:15px;
            border-radius:10px;
            border:1px solid #30363d;
        ">

        <h3 style="
            color:white;
            margin-top:0px;
        ">
            Dashboard Legend
        </h3>

        <ul style="
            color:#d6d6d6;
            margin-bottom:0px;
        ">
        """

        for label, description in legend:

            legend_html += f"""
            <li style="margin-bottom:8px;">
                <b>{label}</b> — {description}
            </li>
            """

        legend_html += """
        </ul>
        </div>
        """

    html = f"""
    <div style="
        font-family:Segoe UI;
        background:#0f1117;
        color:white;
        padding:20px;
        border-radius:10px;
    ">

        <h1 style="
            margin-top:0px;
            margin-bottom:5px;
        ">
            {title}
        </h1>

        <div style="
            color:#9aa4b2;
            margin-bottom:20px;
        ">
            Operational Snapshot
        </div>

        <table style="
            width:100%;
            table-layout:auto;
            border-collapse:collapse;
            background:#1b1f2a;
            border-radius:10px;
            overflow:hidden;
        ">

            <tr style="
                background:#161b22;
            ">

                <th style="
                    text-align:left;
                    padding:12px;
                ">
                    Control
                </th>

                <th style="
                    padding:12px;
                ">
                    Status
                </th>

                <th style="
                    text-align:left;
                    padding:12px;
                ">
                    Operational Reading
                </th>

            </tr>

            {rows}

        </table>

        {action_html}

        {legend_html}

    </div>
    """

    if return_html:
        return html

    return HTML(html)

def render_priority_queue(
    title,
    queue_df,
    legend=None,
    return_html=False
):

    _check_html()

    headers = ""

    for col in queue_df.columns:

        headers += f"""
        <th style="
            text-align:left;
            padding:12px;
            white-space:nowrap;
        ">
            {col}
        </th>
        """

    rows = ""

    for idx, (_, row) in enumerate(
        queue_df.iterrows()
    ):

        background = (
            "#1b1f2a"
            if idx % 2 == 0
            else "#161b22"
        )

        row_html = ""

        for col in queue_df.columns:

            value = row[col]

            colour = "#d6d6d6"
            font_weight = "normal"

            if col.lower() == "criticality":

                criticality = str(value).lower()

                if criticality == "critical":
                    colour = "#c62828"

                elif criticality == "high":
                    colour = "#f57c00"

                else:
                    colour = "#2e7d32"

                font_weight = "bold"

            row_html += f"""
            <td style="
                padding:12px;
                color:{colour};
                font-weight:{font_weight};
                white-space:nowrap;
            ">
                {value}
            </td>
            """

        rows += f"""
        <tr style="
            border-bottom:1px solid #30363d;
            background:{background};
        ">
            {row_html}
        </tr>
        """

    legend_html = ""

    if legend:

        legend_html += """
        <div style="
            margin-top:20px;
            background:#161b22;
            padding:15px;
            border-radius:10px;
            border:1px solid #30363d;
        ">
        <h3 style="
            color:white;
            margin-top:0px;
        ">
            Dashboard Legend
        </h3>
        <ul style="
            color:#d6d6d6;
            margin-bottom:0px;
        ">
        """

        for label, description in legend:

            legend_html += f"""
            <li style="margin-bottom:8px;">
                <b>{label}</b> — {description}
            </li>
            """

        legend_html += """
        </ul>
        </div>
        """

    html = f"""
    <div style="
        font-family:Segoe UI;
        background:#0f1117;
        color:white;
        padding:20px;
        border-radius:10px;
    ">

        <h2 style="
            margin-top:0px;
        ">
            {title}
        </h2>

        <div style="
            overflow-x:auto;
        ">

        <table style="
            width:100%;
            min-width:1200px;
            border-collapse:collapse;
            background:#1b1f2a;
        ">

            <tr style="
                background:#161b22;
            ">

                {headers}

            </tr>

            {rows}

        </table>

        </div>

        {legend_html}

    </div>
    """

    if return_html:
        return html

    return HTML(html)