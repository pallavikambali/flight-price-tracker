from app.price_tracker import check_price


def test_price_within_budget(capsys):
    flight = {"price": 4000}

    check_price(flight, 5000, None)

    output = capsys.readouterr().out
    assert "within your budget" in output


def test_price_above_budget(capsys):
    flight = {"price": 6000}

    check_price(flight, 5000, None)

    output = capsys.readouterr().out
    assert "above your target" in output


def test_price_drop(capsys):
    flight = {"price": 4000}

    check_price(flight, 5000, 5000)

    output = capsys.readouterr().out
    assert "Price dropped by ₹1000" in output


def test_price_increase(capsys):
    flight = {"price": 6000}

    check_price(flight, 7000, 5000)

    output = capsys.readouterr().out
    assert "Price increased by ₹1000" in output