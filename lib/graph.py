data["procent"] = {
    "active": (data["active"] / (data["cases"] // 100) / 5),
    "recovered": (data["recovered"] / (data["cases"] // 100) / 5),
    "deaths": (data["deaths"] / (data["cases"] // 100) / 5),
}

def getFalseSymbol (i, symbol):
    string = ""
    i = int(str(round(i, 0)).replace(".0", ""))
    d = 0
    while d < i:
        string += symbol
        d += 1
    return string

activeStr = getFalseSymbol(data["procent"]["active"], "█")
recoveredStr = getFalseSymbol(data["procent"]["recovered"], "░")
deathsStr = getFalseSymbol(data["procent"]["deaths"], "▒")