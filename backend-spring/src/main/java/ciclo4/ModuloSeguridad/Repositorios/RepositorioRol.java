package ciclo4.ModuloSeguridad.Repositorios;

import ciclo4.ModuloSeguridad.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioRol extends MongoRepository<Rol,String> {
}
