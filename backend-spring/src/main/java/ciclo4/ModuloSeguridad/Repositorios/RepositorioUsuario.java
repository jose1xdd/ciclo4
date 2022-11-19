package ciclo4.ModuloSeguridad.Repositorios;

import org.springframework.data.mongodb.repository.Query;
import ciclo4.ModuloSeguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository<Usuario,String> {
    @Query("{'correo': ?0}")
    public Usuario getUserByEmail(String correo);
}

