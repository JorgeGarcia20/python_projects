from .Usuario import Usuario
from .TipoUsuario import TipoUsuario


class ModeloUsuario():
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id, usuario, password
                        FROM usuario
                        WHERE usuario = '{0}'""".format(usuario.usuario)
            cursor.execute(query)
            data = cursor.fetchone()
            # print(data)
            if data != None:
                match = Usuario.check_password(data[2], usuario.password)
                # print(match)
                if match:
                    logged = Usuario(data[0], data[1], None, None)
                    # print(logged)
                    return logged
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = """SELECT USU.id, USU.usuario, TIP.id, TIP.usuario
                    FROM usuario USU JOIN tipo_usuario TIP ON USU.tipo_usuario = TIP.id
                    WHERE USU.id = {0}""".format(id)
            cursor.execute(query)
            data = cursor.fetchone()
            tipo_usuario = TipoUsuario(data[2], data[3])
            logged_user = Usuario(data[0], data[1], None, tipo_usuario)
            return logged_user
        except Exception as ex:
            raise Exception(ex)
