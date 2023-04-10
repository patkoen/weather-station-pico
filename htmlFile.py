
def website(dht22_temp, dht22_humi, photo):
    head = """
    <!DOCTYPE html>
    <html>
    <head>
        
        <title>PICO</title>
        <style>
            body {background-color: rgb(153, 153, 153);}
            .window {background-color: rgba(0, 0, 0, 0.466); display: flex; justify-content: center;align-items: center;flex-direction: column;border-radius: 10px; padding: 10px;}
            .window .show {background-color: rgb(0, 0, 0); box-sizing: border-box; border-radius: 10px; border-style: solid;}
            .row {min-width: 400px; display: flex; justify-content: space-between;align-items: center;border-radius: 10px;padding: 10px;margin: 5px 0 0; background-color: rgb(114, 114, 114); color: rgb(216, 216, 216);}
            h1 {display: flex; justify-content: center; border-radius: 10px; padding: 10px; margin: 0 0; background-color: rgb(114, 114, 114); color: rgb(216, 216, 216);}
            .col-left {margin-right: auto;}
            .col-right {margin-left: auto;}
            .diagramm {font-family: 'Helvetica Neue', sans-serif; gap: 0.4em; padding: 10px 20px; background-color: rgb(114, 114, 114); height: 200px; transform: rotate(180deg); display: flex; flex-direction: row-reverse; border-radius: 10px;}
            .diagramm>div {height: calc(var(--p) * 1%); background-color: rgb(17, 112, 255); display: flex; width: 3%; justify-content: center; align-items: flex-end; font-size: 1.2rem;font-weight: bold; transform: scaleY(-1); transform: rotate(180deg); border-radius: 10px;}
            h6 {transform: rotate(-90deg); position: absolute; top: -20px;}
            h3 {display: flex; justify-content: center; border-radius: 10px; padding: 10px; margin: 0 0; background-color: rgb(114, 114, 114); color: rgb(216, 216, 216); margin: 5px 0;}
            h2 {display: flex; justify-content: center; border-radius: 10px; padding: 10px; margin: 0 0; background-color: rgb(114, 114, 114); color: rgb(216, 216, 216); margin: 5px 0;}
            .chart-container {max-width: 500px; margin: 0 auto; text-align: center;}
            svg {width: 100%; stroke: "none";}
            .axis text {font-size: 12px; fill: #999;}
            .grid line {stroke: #0661ca; stroke-dasharray: 2;}
            .grid2 line {stroke: #c7ca06;stroke-dasharray: 2;}
            polyline {fill: none;stroke-linecap: round;stroke-width: 3;}
        </style>
    </head>
    """
    show_data = """
    <body>
        <div class="window">
            <div class="show">
                <h1>Pico Wetter</h1>
                <div class="row"><div class="col-left">Temperatur:</div><div class="col-right">{}&deg;C</div></div>
                <div class="row"><div class="col-left">Luftfeuchtigkeit:</div><div class="col-right"> {} %</div></div>
                <div class="row"><div class="col-left">Licht:</div><div class="col-right"> {} </div></div>
                """
    svg_start = """
                <div>
                    <div class="chart-container">
                        <h3>Verlauf:</h3>
                        <svg width="500" height="300">
                            <g class="grid">
                                <line x1="0" y1="10" x2="500" y2="10" /><line x1="0" y1="60" x2="500" y2="60" /><line x1="0" y1="110" x2="500" y2="110" /><line x1="0" y1="160" x2="500" y2="160" /><line x1="0" y1="210" x2="500" y2="210" /><line x1="0" y1="260" x2="500" y2="260" />
                                <line x1="0" y1="0" x2="0" y2="280" /><line x1="50" y1="0" x2="50" y2="280" /><line x1="100" y1="0" x2="100" y2="280" /><line x1="150" y1="0" x2="150" y2="280" /><line x1="200" y1="0" x2="200" y2="280" /><line x1="250" y1="0" x2="250" y2="280" /><line x1="300" y1="0" x2="300" y2="280" /><line x1="350" y1="0" x2="350" y2="280" /><line x1="400" y1="0" x2="400" y2="280" /><line x1="450" y1="0" x2="450" y2="280" />
                            </g>
                            <g class="axis">
                                <text x="10" y="10">40</text><text x="10" y="60">30</text><text x="10" y="110">20</text><text x="10" y="160">10</text><text x="10" y="210">0</text><text x="10" y="260">-10</text>
                            </g>
                            <g class="grid2">
                                <line x1="0" y1="30" x2="500" y2="30" /><line x1="0" y1="60" x2="500" y2="60" /><line x1="0" y1="90" x2="500" y2="90" /><line x1="0" y1="120" x2="500" y2="120" /><line x1="0" y1="150" x2="500" y2="150" /><line x1="0" y1="180" x2="500" y2="180" /><line x1="0" y1="210" x2="500" y2="210" /><line x1="0" y1="240" x2="500" y2="240" /><line x1="0" y1="270" x2="500" y2="270" /><line x1="0" y1="300" x2="500" y2="300" />
                            </g>
                            <g class="axis">
                                <text x="480" y="0">100</text><text x="480" y="30">90</text><text x="480" y="60">80</text><text x="480" y="90">70</text><text x="480" y="120">60</text><text x="480" y="150">50</text><text x="480" y="180">40</text><text x="480" y="210">30</text><text x="480" y="240">20</text><text x="480" y="270">10</text><text x="480" y="300">0</text>
                            </g>
                            """
    svg_temp = """
                            <polyline points="20, {} 30, {} 40, {} 50, {} 60, {} 70, {} 80, {} 90, {} 100, {} 110, {} 120, {} 130, {} 140, {} 150, {} 160, {} 170, {} 180, {} 190, {} 200, {} 210, {} 220, {} 230, {} 240, {} 250, {} 260, {} 270, {} 280, {} 290, {} 300, {} 310, {} 320, {} 330, {} 340, {} 350, {} 360, {} 370, {} 380, {} 390, {} 400, {} 410, {} 420, {} 430, {} 440, {} 450, {} 460, {} 470, {} 480, {} 490, {} " stroke="red" />
                            """
    svg_humi = """
                            <polyline points="20, {} 30, {} 40, {} 50, {} 60, {} 70, {} 80, {} 90, {} 100, {} 110, {} 120, {} 130, {} 140, {} 150, {} 160, {} 170, {} 180, {} 190, {} 200, {} 210, {} 220, {} 230, {} 240, {} 250, {} 260, {} 270, {} 280, {} 290, {} 300, {} 310, {} 320, {} 330, {} 340, {} 350, {} 360, {} 370, {} 380, {} 390, {} 400, {} 410, {} 420, {} 430, {} 440, {} 450, {} 460, {} 470, {} 480, {} 490, {} " stroke="blue" />
                            """
    svg_end = """
                        </svg>
                    </div>
                </div>
                """
    end = """
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    data=[dht22_temp[len(dht22_temp)-1],dht22_humi[len(dht22_humi)-1],photo[len(photo)-1]]
    show_data = show_data.format(*data)
    
    x=[]
    for i in dht22_temp:
        temp = 210-(i*5)
        x.append(temp)
    
    y=[]
    for i in dht22_humi:
        hy = 280 - (i*2.8)
        y.append(hy)
    
    svg_temp = svg_temp.format(*x)
    svg_humi = svg_humi.format(*y)
    
    return head + show_data + svg_start + svg_temp + svg_humi + svg_end + end









