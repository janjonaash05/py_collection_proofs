# Opravte níže uvedené funkce tak, aby nebyly náchylné k HTML a XML Injection pouzij reg ex nebo jiny string processing:

def build_html_contact_item(name, phone):
    return '<div class="contact_item"><h2>"+name+"</h2><p>Phone: "+phone+"</p></div>'

def build_html_img(path, width, height, description=""):
    return "<img src=""+path+"" alt=""+description+"" width=""+str(width)+"" height=""+str(height)+"">"

def build_xml_from_money_transactions(money_transactions):
    xml = "<money_transactions>\n"
    for transaction in money_transactions:
        xml += " <transaction>\n"
        xml += "  <account_number>" + transaction["account_number"] + "</account_number>\n"
        xml += "  <amount>" + str(transaction["amount"]) + "</amount>\n"
        xml += "  <message>" + transaction["message"] + "</message>\n"
        xml += " </transaction>\n"
    xml += "</money_transactions>\n"
    return xml
Po opravě musí být zachováná funkčnost níže uvedených příkladů:
print(build_html_contact_item("Ing. Jan Novák","+420 606321423"))
print(build_html_img("/img/obrazek.jpg",80,40,"Logo firmy"))
print(build_xml_from_money_transactions([
    {"account_number" : "0500021502/0800","amount":1300, "message":"Platba za obědy Jan Novák"},
    {"account_number" : "1500023322/0600","amount":1450, "message":"Obědy Petr Novák"}
]))
Ukázky možné HTML a XML Injection (a také i XSS) si můžete prohlédnout:
print(build_html_contact_item("Ing. Jan Novák","+420 606321423</p></div><script>alert('Hacked!');</script><p><div>"))
print(build_html_img("/img/obrazek.jpg",80,40,""/><img src="" width="100" height="200" alt="Hacked logo"))
print(build_xml_from_money_transactions([
    {"account_number": "0500021502/0800",  "amount": 1300, "message": "Platba za obědy Jan Novák"},
    {"account_number": "1500023322/0600",  "amount": 1450, "message": "Obědy Petr Novák</message>\n </transaction>\n <transaction>\n  <account_number>0700098720/0100</account_number>\n  <amount>1000000</amount>\n  <message>Hack"}
]))