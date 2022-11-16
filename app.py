import gradio as gr
from forecast import optimizer

year_list = [*range(2000, 2023)] # using unpacking operator 
month_list = [*range(1,13)]
day_list = [*range(1, 32)]
stock_tickers = ["TSLA", "GOOGL", "AAPL", "AMZN", "META"]
etf_tickers = ["SPY", "IWM", "QQQ", "DIA", "GLD"]
#asset_classes_ticker = []

with gr.Blocks() as demo:
    error_box = gr.Textbox(label="Error", visible=False)

    gr.Markdown("Please choose at least two ticker symbol:")
    with gr.Row():
        with gr.Column():
            stock_tickers = gr.CheckboxGroup(label="Stocks", choices=stock_tickers)
        with gr.Column():
            etf_tickers = gr.CheckboxGroup(label="ETFs", choices=etf_tickers)
            #gr.CheckboxGroup(label="Asset classes", choices=asset_classes_ticker)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("Please select a start date:")
            start_year = gr.Dropdown(label="Year", choices=year_list)
            start_month = gr.Dropdown(label="Month", choices=month_list)
            start_day = gr.Dropdown(label="Day", choices=day_list)
        with gr.Column():
            gr.Markdown("Please select an end date:")
            end_year = gr.Dropdown(label="Year", choices=year_list)
            end_month = gr.Dropdown(label="Month", choices=month_list)
            end_day = gr.Dropdown(label="Day", choices=day_list)
        with gr.Column():
            gr.Markdown("Please select a frequency:")
    
    submit_btn = gr.Button("Submit")

    with gr.Row(visible=False) as output_row:
        results_box = gr.Textbox(label="RESULTS!")

    def submit(stock_tickers, etf_tickers, start_year, start_month, start_day, end_year, end_month, end_day):
        # check if tickers were selected
        selected_tickers = stock_tickers + etf_tickers
        if len(selected_tickers) <=  1:
            return {error_box: gr.update(value="Select at least two ticker", visible=True)}

        # formatting input data
        selected_tickers = stock_tickers + etf_tickers
        start_date = f'{start_year}-{start_month}-{start_day}'
        end_date = f'{end_year}-{end_month}-{end_day}'

        # example message to be deleted when model is integrated
        message = "Tickers selected: "
        for ticker in selected_tickers:
            message = message + ticker + ", "

        message = message + f'from {start_date} to {end_date}.'

        optimizer.optimize(selected_tickers, start_date, end_date)

        return {
            output_row: gr.update(visible=True),
            results_box: message
        }

    submit_btn.click(
        fn=submit, # function being called
        inputs=[stock_tickers, etf_tickers, start_year, start_month, start_day, end_year, end_month, end_day], 
        outputs=[output_row, results_box, error_box]
    )

demo.launch()