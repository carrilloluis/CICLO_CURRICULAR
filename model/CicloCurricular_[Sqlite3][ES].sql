CREATE TABLE IF NOT EXISTS [Ciclo Curricular] (
	[id] CHAR(36) NOT NULL PRIMARY KEY,
	[fecha de vigencia] DATE NOT NULL, 
	[ciclo numérico] INTEGER NOT NULL,
	-- **Notación** del Ciclo Curricular
	[descripción] TEXT NOT NULL,
	[estados] INTEGER NOT NULL
) WITHOUT ROWID;