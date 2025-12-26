
def position_size(balance, risk_percent, stop_loss):
    try:
        balance = float(balance)
        risk_percent = float(risk_percent)
        stop_loss = float(stop_loss)
        size = (balance * (risk_percent / 100)) / stop_loss
        return round(size, 2)

    except:
        return None

def profit_loss(entry, exit_price, position_size):
    try:
        entry = float(entry)
        exit_price = float(exit_price)
        position_size = float(position_size)
        pl = (exit_price - entry ) * position_size
        return round(pl, 2)
    except:
        return None

def leverage_position(balance, leverage, risk_percent, stop_loss):
    try:
        balance = float(balance)
        leverage = float(leverage)
        risk_percent = float(risk_percent)
        stop_loss = float(stop_loss)
        size = (balance * (risk_percent / 100) * leverage) / stop_loss
        return round(size, 2)
    except:
        return None

