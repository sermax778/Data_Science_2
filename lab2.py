from spyre import server
import lab1


DATASET = lab1.get_dataset()
print(DATASET.head())

class StockExample(server.App):
    title = "NOAA data vizualization"

    inputs = [{
        "type": 'dropdown',
        "label": 'NOAA data dropdown',
        "options": [
            {"label": "VCI", "value": "VCI"},
            {"label": "TCI", "value": "TCI"},
            {"label": "VHI", "value": "VHI"}
        ],
        "key": 'ticker1',
        "action_id": "update_data"
    },
    {
        "type": 'dropdown',
        "label": 'Area',
        "options": [
            {"label": "Вінницька", "value": "1"},
            {"label": "Волинська", "value": "2"},
            {"label": "Дніпропетровська", "value": "3"},
            {"label": "Донецька", "value": "4"},
            {"label": "Житомирська", "value": "5"},
            {"label": "Закарпатська", "value": "6"},
            {"label": "Запорізька", "value": "7"},
            {"label": "Івано-Франківська", "value": "8"},
            {"label": "Київська", "value": "9"},
            {"label": "Кіровоградська", "value": "10"},
            {"label": "Луганська", "value": "11"},
            {"label": "Львівська", "value": "12"},
            {"label": "Миколаївська", "value": "13"},
            {"label": "Одеська", "value": "14"},
            {"label": "Полтавська", "value": "15"},
            {"label": "Рівенська", "value": "16"},
            {"label": "Сумська", "value": "17"},
            {"label": "Тернопільська", "value": "18"},
            {"label": "Харківська", "value": "19"},
            {"label": "Херсонська", "value": "20"},
            {"label": "Хмельницька", "value": "21"},
            {"label": "Черкаська", "value": "22"},
            {"label": "Чернівецька", "value": "23"},
            {"label": "Чернігівська", "value": "24"},
            {"label": "Республіка Крим", "value": "25"}
        ],
        "key": 'ticker2',
        "action_id": "update_data"
    },
    {
        "type": 'text',
        "label": 'Range of weeks',
        "value": '9-10',
        "key": 'range',
        "action_id": "simple_html_output"
    }
    ]

    controls = [{
        "type": "hidden",
        "id": "update_data"
    }]

    tabs = ["Plot", "Table"]

    outputs = [
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"
        },
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        }
    ]

    def getData(self, params):
        range_w = params['range']
        ranges = range_w.split('-')
        # ranges = self.HTMLhandler(self.getHTML(params['range']))
        ranges = [int(ranges[0]), int(ranges[1])]
        ticker1 = params['ticker1']
        ticker2 = params['ticker2']
        # df = DATASET.loc[(DATASET['area'] == ticker2) & (DATASET['Week'] <= ranges[1]) & (DATASET['Week'] >= ranges[0])]
        # df = df[ticker1]
        df = DATASET.loc[(DATASET['area'] == ticker2) &
                         (DATASET['Week'] <= ranges[1]) &
                         (DATASET['Week'] >= ranges[0]),
                         [ticker1, "Week", "Year"]]
        print(df)
        return df


    def getPlot(self, params):
        range_w = params['range']
        ranges = range_w.split('-')
        # ranges = self.HTMLhandler(self.getHTML(params['range']))
        ranges = [int(ranges[0]), int(ranges[1])]
        ticker1 = params['ticker1']
        ticker2 = params['ticker2']
        # df = DATASET.loc[(DATASET['area'] == ticker2) & (DATASET['Week'] <= ranges[1]) & (DATASET['Week'] >= ranges[0])]
        # df = df[ticker1]
        df = DATASET.loc[(DATASET['area'] == ticker2) & (DATASET['Week'] <= ranges[1]) & (DATASET['Week'] >= ranges[0]), [ticker1, "Year"]]
        df = df.set_index('Year')
        plt_obj = df.plot()

        plt_obj.set_xlabel("Year")
        plt_obj.set_ylabel(ticker1)

        fig = plt_obj.get_figure()
        return fig


app = StockExample()
app.launch(port=4000)
