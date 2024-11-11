from app.repositories.point_repository import PointRepository
import datetime


class PointUseCase:
    def __init__(self):
        self.point_repository = PointRepository()
    
    def create_point(self, point_data):
        return self.point_repository.create(point_data)
    
    def get_point_by_id(self, point_id):
        return self.point_repository.get_by_id(point_id)
    
    def get_all_points(self):
        return self.point_repository.get_all()
    
    def update_point(self, point_id, point_data):
        ponto = self.point_repository.get_by_id(point_id)
        if ponto is None:
            return None
        ponto = ponto.dict()
        if ponto.pause == False:
            ponto.pause = True
            data_banco, tempo_banco = ponto.total_hours.split(' ')
            hora_banco, minuto_banco, segundos_banco = tempo_banco.split(':')
            ano_banco, mes_banco, dia_banco = data_banco.split('-')
            hora_banco = datetime.datetime(year= ano_banco, month=mes_banco, day=dia_banco,  hour=hora_banco, minute=minuto_banco, second=segundos_banco)
            
            data_atual, tempo_atual = point_data.split()
            hora_atual, minuto_atual, segundos_atual = tempo_atual.split(':')
            hora_atual = datetime.datetime(hour=hora_atual, minute=minuto_atual, second=segundos_atual)
            ano_atual, mes_atual, dia_atual = data_atual.split('-')
            
            if ano_banco == ano_atual and mes_banco == mes_atual and dia_banco == dia_atual:
                total_hours_work = hora_banco + hora_atual
                ponto.total_hours = total_hours_work
        else:
            ponto.pause = False

        return self.point_repository.update(point_id, ponto)
    
    def delete_point(self, point_id):
        return self.point_repository.delete(point_id)