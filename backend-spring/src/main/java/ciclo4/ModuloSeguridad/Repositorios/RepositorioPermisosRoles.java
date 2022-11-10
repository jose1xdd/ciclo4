package ciclo4.ModuloSeguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import ciclo4.ModuloSeguridad.Modelos.PermisosRoles;


public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String> {
}
