CREATE TABLE rrhh.hired_employees (
    id INT NOT NULL,
    name VARCHAR(255),
    datetime DATETIME,
    department_id INT,
    job_id INT,
    UNIQUE (id)  
);
CREATE TABLE rrhh..departments (
    id INT NOT NULL,
    department VARCHAR(255),
    UNIQUE (id)  
);
CREATE TABLE rrhh.jobs(
    id INT NOT NULL,
    job VARCHAR(255),
    UNIQUE (id)  
);