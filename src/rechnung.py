from jinja2 import Template

def generate_invoice(booking_id,
                    room_id,
                    room_name,
                    user_id,
                    username,
                    firstname,
                    lastname,
                    street,
                    city,
                    postcode,
                    price,
                    steuer):
    # Daten für die Rechnung
    rechnung = {
        "buchungs_id": booking_id,
        "raum_id": room_id,
        "raum_name": room_name,
        "nutzer_id": user_id,
        "username": username,
        "vorname": firstname,
        "nachname": lastname,
        "strasse": street,
        "stadt": city,
        "postleitzahl": postcode,
        "buchungszeitraum": "01.01.2023 - 07.01.2023",  # Beispielwert
        "preis": price,
        "mehrwertsteuer": steuer
    }

    # HTML-Vorlage für die Rechnung
    html_template = """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Rechnung</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .invoice-box { max-width: 800px; margin: auto; padding: 30px; border: 1px solid #eee; box-shadow: 0 0 10px rgba(0, 0, 0, 0.15); }
            .invoice-box table { width: 100%; line-height: inherit; text-align: left; }
            .invoice-box table td { padding: 5px; vertical-align: top; }
            .invoice-box table tr td:nth-child(2) { text-align: right; }
            .invoice-box table tr.top table td { padding-bottom: 20px; }
            .invoice-box table tr.top table td.title { font-size: 45px; line-height: 45px; color: #333; }
            .invoice-box table tr.information table td { padding-bottom: 40px; }
            .invoice-box table tr.heading td { background: #eee; border-bottom: 1px solid #ddd; font-weight: bold; }
            .invoice-box table tr.details td { padding-bottom: 20px; }
            .invoice-box table tr.item td { border-bottom: 1px solid #eee; }
            .invoice-box table tr.item.last td { border-bottom: none; }
            .invoice-box table tr.total td:nth-child(2) { border-top: 2px solid #eee; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="invoice-box">
            <table cellpadding="0" cellspacing="0">
                <tr class="top">
                    <td colspan="2">
                        <table>
                            <tr>
                                <td class="title">
                                    <h2>Rechnung</h2>
                                </td>
                                <td>
                                    Rechnungsnummer: {{ buchungs_id }}<br>
                                    Erstellt am: {{ erstellungsdatum }}<br>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr class="information">
                    <td colspan="2">
                        <table>
                            <tr>
                                <td>
                                    Raum-ID:<br>
                                    Raum-Name:<br>
                                    Nutzer-ID:<br>
                                    Benutzername:<br>
                                    Vorname:<br>
                                    Nachname:<br>
                                    Strasse:<br>
                                    Stadt:<br>
                                    Postleitzahl:<br>
                                    Buchungszeitraum:<br>
                                </td>
                                <td>
                                    {{ raum_id }}<br>
                                    {{ raum_name }}<br>
                                    {{ nutzer_id }}<br>
                                    {{ username }}<br>
                                    {{ vorname }}<br>
                                    {{ nachname }}<br>
                                    {{ strasse }}<br>
                                    {{ stadt }}<br>
                                    {{ postleitzahl }}<br>
                                    {{ buchungszeitraum }}<br>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr class="heading">
                    <td>Beschreibung</td>
                    <td>Betrag</td>
                </tr>
                <tr class="item">
                    <td>Preis</td>
                    <td>{{ preis }}</td>
                </tr>
                <tr class="item last">
                    <td>Mehrwertsteuer</td>
                    <td>{{ mehrwertsteuer }}</td>
                </tr>
                <tr class="total">
                    <td></td>
                    <td>Gesamtbetrag: {{ gesamtbetrag }}</td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    """

    # Berechnung des Gesamtbetrags
    preis = float(rechnung["preis"].replace(",", ".").replace(" EUR", ""))
    mehrwertsteuer = float(rechnung["mehrwertsteuer"].replace("%", "")) / 100
    gesamtbetrag = preis * (1 + mehrwertsteuer)
    rechnung["gesamtbetrag"] = f"{gesamtbetrag:.2f} EUR"
    rechnung["erstellungsdatum"] = "01.01.2023"  # Beispielwert

    # HTML mit den Rechnungsdaten rendern
    template = Template(html_template)
    html_content = template.render(**rechnung)

    # HTML in eine Datei schreiben
    with open("rechnung.html", "w") as f:
        f.write(html_content)

    print("Die Rechnung wurde erfolgreich in 'rechnung.html' erstellt.")

# Beispielaufruf der Funktion
generate_invoice(
    booking_id="123456",
    room_id="A101",
    room_name="Konferenzraum",
    user_id="U7890",
    username="johndoe",
    firstname="John",
    lastname="Doe",
    street="Musterstrasse 1",
    city="Musterstadt",
    postcode="12345",
    price="500,00 EUR",
    steuer="19%"
)