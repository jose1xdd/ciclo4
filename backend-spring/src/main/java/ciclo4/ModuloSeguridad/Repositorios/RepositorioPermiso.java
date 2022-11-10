package ciclo4.ModuloSeguridad.Repositorios;

import ciclo4.ModuloSeguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioPermiso extends MongoRepository<Permiso,String> {
}
