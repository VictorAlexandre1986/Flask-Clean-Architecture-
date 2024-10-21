from app.models.enterprise import Enterprise,get_db


class EnterpriseRepository:
    def create(self, data):
        db = get_db()
        enterprise = Enterprise(name=data.name, 
                           email=data.email,
                           phoneNumber=data.phoneNumber,
                           id_login=data.id_login,
                           address=data.address,
                           city=data.city,
                           state=data.state,
                           cep=data.cep,
                           number=data.number,
                           complement=data.complement,
                           cnpj=data.cnpj
                           )

        db.session.add(enterprise)
        db.session.commit()
        return enterprise

    def get_by_id(self, enterprise_id):
        return Enterprise.query.get(enterprise_id)
    
    def get_all(self):
        return Enterprise.query.all()
    
    def update(self, enterprise_id, data):
        db = get_db()
        enterprise = Enterprise.query.get(enterprise_id)
        if enterprise:
            enterprise.username = data.username
            enterprise.email = data.email
            enterprise.phoneNumber = data.phoneNumber
            enterprise.id_login = data.id_login
            enterprise.address = data.address
            enterprise.city = data.city
            enterprise.state = data.state
            enterprise.cep = data.cep
            enterprise.number = data.number
            enterprise.complement = data.complement
            enterprise.cnpj = data.cnpj
            db.session.commit()
        return enterprise
    
    def delete(self, enterprise_id):
        db = get_db()
        enterprise = Enterprise.query.get(enterprise_id)
        if enterprise:
            db.session.delete(enterprise)
            db.session.commit()
        return enterprise