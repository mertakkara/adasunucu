import flask
from flask import jsonify
from flask import request



app = flask.Flask(__name__)

@app.route('/response/', methods = ['POST'])
def response():
	msg_received2 = flask.request.get_json()
	result = [
	
	
	]
	
	
	if(msg_received2["KisilerFarkliVagonlaraYerlestirilebilir"]):
		tren = msg_received2["Tren"]
		kisi = msg_received2["RezervasyonYapilacakKisiSayisi"]
		for item in tren['Vagonlar']:
			kapasite = ((item['Kapasite'] / 100) * 70) 
			DoluKoltukAdet = item['DoluKoltukAdet']
			if(kapasite>=DoluKoltukAdet):
				newkisi = kisi - (kapasite - DoluKoltukAdet)
				if(newkisi<=0):
					result.append({'VagonAdi':item['Ad'], 'KisiSayisi':int(kisi)})
					return jsonify( 
						RezervasyonYapilabilir= True,
						YerlesimAyrinti = result
					)
				else:
					kisi = newkisi 
					eklenen =(int) (kapasite - DoluKoltukAdet)
					result.append({'VagonAdi':item['Ad'], 'KisiSayisi':eklenen})
					
				
			
		emptyresult = []
		return jsonify(
					RezervasyonYapilabilir  = True,
					YerlesimAyrinti = emptyresult
				)
	else:
		tren = msg_received2["Tren"]
		for item in tren['Vagonlar']:
			kapasite = ((item['Kapasite'] / 100) * 70) 
			kisi = msg_received2["RezervasyonYapilacakKisiSayisi"]
			if(kapasite >=(item['DoluKoltukAdet']+ kisi)):
				result.append({'VagonAdi':item['Ad'], 'KisiSayisi':int(kisi)})
				return jsonify(
					RezervasyonYapilabilir= True,
					YerlesimAyrinti = result
				)
		emptyresult = []
		return jsonify(
					RezervasyonYapilabilir  = True,
					YerlesimAyrinti = emptyresult
				)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)