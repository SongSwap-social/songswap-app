# app/blueprints/insights/routes.py
from flask import Blueprint, render_template
from pyecharts import options as opts
from pyecharts.charts import Bar
import json

insights_bp = Blueprint("insights", __name__)


@insights_bp.route("/insights")
def home():
    import random
    import datetime

    import pyecharts.options as opts
    from pyecharts.charts import Calendar

    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range((end - begin).days + 1)
    ]

    chart = (
        Calendar()
        .add(
            series_name="",
            yaxis_data=data,
            calendar_opts=opts.CalendarOpts(
                pos_top="120",
                pos_left="30",
                pos_right="30",
                range_="2017",
                yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                pos_top="30", pos_left="center", title="2017年步数情况"
            ),
            visualmap_opts=opts.VisualMapOpts(
                max_=25000, min_=500, orient="horizontal", is_piecewise=False
            ),
        )
        .dump_options()
    )

    import random

    from pyecharts import options as opts
    from pyecharts.charts import HeatMap
    from pyecharts.faker import Faker

    value = [[i, j, random.randint(0, 80)] for i in range(24) for j in range(7)]
    c = (
        HeatMap()
        .add_xaxis(Faker.clock)
        .add_yaxis(
            "series0",
            [w.strip("day") for w in Faker.week_en],
            value,
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="HeatMap-Label"),
            visualmap_opts=opts.VisualMapOpts(),
        )
        .dump_options()
    )

    return render_template("insights.html", chart=chart)
