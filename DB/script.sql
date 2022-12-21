-- -----------------------------------------------------
-- Table `colegio`.`direccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`direccion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ciudad` VARCHAR(45) NOT NULL,
  `calle` VARCHAR(45) NOT NULL,
  `numero` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`institucion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`institucion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `direccion_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FKinstitucionDireccion_idx` (`direccion_id` ASC),
  CONSTRAINT `FKinstitucionDireccion`
    FOREIGN KEY (`direccion_id`)
    REFERENCES `colegio`.`direccion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellidoPaterno` VARCHAR(45) NOT NULL,
  `apellidoMaterno` VARCHAR(45) NULL,
  `direccion_id` INT NULL,
  `nacimiento` DATETIME NULL,
  `estado` TINYINT NOT NULL,
  `institucion_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FKdireccionUsuario_idx` (`direccion_id` ASC),
  INDEX `FKinstitucionUsuario_idx` (`institucion_id` ASC) ,
  CONSTRAINT `FKdireccionUsuario`
    FOREIGN KEY (`direccion_id`)
    REFERENCES `colegio`.`direccion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FKinstitucionUsuario`
    FOREIGN KEY (`institucion_id`)
    REFERENCES `colegio`.`institucion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`profesor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`profesor` (
  `usuario_id` INT NOT NULL,
  `titulo` VARCHAR(45) NULL,
  `puntuacion` VARCHAR(45) NULL,
  PRIMARY KEY (`usuario_id`),
  CONSTRAINT `FKusuarioId`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `colegio`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`curso` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`alumno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`alumno` (
  `usuario_id` INT NOT NULL,
  `curso_id` INT NOT NULL,
  `promedio` DECIMAL NOT NULL,
  PRIMARY KEY (`usuario_id`),
  INDEX `FKalumnoCurso_idx` (`curso_id` ASC) ,
  CONSTRAINT `FKalumnoUsuario`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `colegio`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FKalumnoCurso`
    FOREIGN KEY (`curso_id`)
    REFERENCES `colegio`.`curso` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`asignatura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`asignatura` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`calificacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`calificacion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `alumno_id` INT NOT NULL,
  `asignatura_id` INT NOT NULL,
  `profesor_id` INT NOT NULL,
  `fecha` DATETIME NOT NULL,
  `nota` DECIMAL NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FKcalificacionAlumno_idx` (`alumno_id` ASC) ,
  INDEX `FKcalificacionProfesor_idx` (`profesor_id` ASC) ,
  INDEX `FKcalificacionAsignatura_idx` (`asignatura_id` ASC) ,
  CONSTRAINT `FKcalificacionAlumno`
    FOREIGN KEY (`alumno_id`)
    REFERENCES `colegio`.`alumno` (`usuario_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FKcalificacionProfesor`
    FOREIGN KEY (`profesor_id`)
    REFERENCES `colegio`.`profesor` (`usuario_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FKcalificacionAsignatura`
    FOREIGN KEY (`asignatura_id`)
    REFERENCES `colegio`.`asignatura` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

