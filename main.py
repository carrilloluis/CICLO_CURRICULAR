import bottle
import sqlite3
import json
import uuid
from contextlib import closing

app = application = bottle.Bottle()

MINIMAL_CORS = {
	'Content-type' : 'application/json',
	'Access-Control-Allow-Origin' : 'localhost:8093',
}

DB_PATH = '/mnt/sdcard/CicloCurricular.db'

@app.route("/<filepath:re:.*\.(css|js)>", method='GET')
def asset_files(filepath):
	return bottle.static_file(filepath, root='./static/')

@app.error(404)
def error404(error):
	return 'Nothing here, sorry'


@app.route('/CICLO_CURRICULAR/v1/', method='GET')
def get_courses():
	try:
		with sqlite3.connect(DB_PATH) as connection:
			with closing(connection.cursor()) as cursor:
				cursor.execute("SELECT UPPER([id]) AS id, UPPER([descripción]) AS nm, (([estados] & 1) = 1) AS e FROM [Ciclo Curricular]", ())
				cursor.row_factory = sqlite3.Row
				ds_ = [dict(r) for r in cursor.fetchall()]
				return bottle.HTTPResponse(body=json.dumps({'data': ds_}), status=200, headers=MINIMAL_CORS)
	except sqlite3.OperationalError as e:
		return bottle.HTTPResponse(body=json.dumps({'msg': str(e)}), status=500)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8093, reloader=True, debug=True)