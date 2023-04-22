-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.3
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
CREATE DATABASE new_database;
-- ddl-end --


-- object: factory_control | type: SCHEMA --
-- DROP SCHEMA IF EXISTS factory_control CASCADE;
CREATE SCHEMA factory_control;
-- ddl-end --
ALTER SCHEMA factory_control OWNER TO postgres;
-- ddl-end --
COMMENT ON SCHEMA factory_control IS E'схема автоматизированной системы контроля предприятия';
-- ddl-end --

SET search_path TO pg_catalog,public,factory_control;
-- ddl-end --

-- object: factory_control.person | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.person CASCADE;
CREATE TABLE factory_control.person (
	id_pk uuid NOT NULL,
	name varchar(255),
	second_name varchar(255),
	surname varchar(255),
	code_pk_department varchar(4),
	code_pk_job varchar(10),
	code_pk_project uuid,
	CONSTRAINT person_id_pk PRIMARY KEY (id_pk)

);
-- ddl-end --
ALTER TABLE factory_control.person OWNER TO postgres;
-- ddl-end --

-- object: factory_control.department | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.department CASCADE;
CREATE TABLE factory_control.department (
	code_pk varchar(4) NOT NULL,
	name varchar(255),
	director varchar(255),
	CONSTRAINT department_code_pk PRIMARY KEY (code_pk)

);
-- ddl-end --
ALTER TABLE factory_control.department OWNER TO postgres;
-- ddl-end --

-- object: factory_control.job | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.job CASCADE;
CREATE TABLE factory_control.job (
	code_pk varchar(10) NOT NULL,
	name varchar(255),
	salary float8,
	CONSTRAINT code_pk PRIMARY KEY (code_pk)

);
-- ddl-end --
ALTER TABLE factory_control.job OWNER TO postgres;
-- ddl-end --

-- object: factory_control.timetable | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.timetable CASCADE;
CREATE TABLE factory_control.timetable (
	person_id_fk uuid,
	time_begin time,
	time_end time,
	data text,
	id_pk uuid NOT NULL,
	id_pk_person uuid,
	CONSTRAINT id_pk PRIMARY KEY (id_pk)

);
-- ddl-end --
ALTER TABLE factory_control.timetable OWNER TO postgres;
-- ddl-end --

-- object: factory_control."order" | type: TABLE --
-- DROP TABLE IF EXISTS factory_control."order" CASCADE;
CREATE TABLE factory_control."order" (
	code uuid NOT NULL,
	name varchar(255),
	creation_date date,
	status varchar(255),
	data text,
	code_pk_department varchar(4),
	CONSTRAINT order_code_pk PRIMARY KEY (code)

);
-- ddl-end --
ALTER TABLE factory_control."order" OWNER TO postgres;
-- ddl-end --

-- object: department_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control."order" DROP CONSTRAINT IF EXISTS department_fk CASCADE;
ALTER TABLE factory_control."order" ADD CONSTRAINT department_fk FOREIGN KEY (code_pk_department)
REFERENCES factory_control.department (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: department_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.person DROP CONSTRAINT IF EXISTS department_fk CASCADE;
ALTER TABLE factory_control.person ADD CONSTRAINT department_fk FOREIGN KEY (code_pk_department)
REFERENCES factory_control.department (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: person_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.timetable DROP CONSTRAINT IF EXISTS person_fk CASCADE;
ALTER TABLE factory_control.timetable ADD CONSTRAINT person_fk FOREIGN KEY (id_pk_person)
REFERENCES factory_control.person (id_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: job_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.person DROP CONSTRAINT IF EXISTS job_fk CASCADE;
ALTER TABLE factory_control.person ADD CONSTRAINT job_fk FOREIGN KEY (code_pk_job)
REFERENCES factory_control.job (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: factory_control.purchases | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.purchases CASCADE;
CREATE TABLE factory_control.purchases (
	code_pk_department varchar(4),
	code_order uuid
);
-- ddl-end --
ALTER TABLE factory_control.purchases OWNER TO postgres;
-- ddl-end --

-- object: factory_control.project | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.project CASCADE;
CREATE TABLE factory_control.project (
	code_pk_department varchar(4),
	code_pk uuid NOT NULL,
	CONSTRAINT project_code_pk PRIMARY KEY (code_pk)

);
-- ddl-end --
ALTER TABLE factory_control.project OWNER TO postgres;
-- ddl-end --

-- object: department_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.project DROP CONSTRAINT IF EXISTS department_fk CASCADE;
ALTER TABLE factory_control.project ADD CONSTRAINT department_fk FOREIGN KEY (code_pk_department)
REFERENCES factory_control.department (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: department_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.purchases DROP CONSTRAINT IF EXISTS department_fk CASCADE;
ALTER TABLE factory_control.purchases ADD CONSTRAINT department_fk FOREIGN KEY (code_pk_department)
REFERENCES factory_control.department (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: order_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.purchases DROP CONSTRAINT IF EXISTS order_fk CASCADE;
ALTER TABLE factory_control.purchases ADD CONSTRAINT order_fk FOREIGN KEY (code_order)
REFERENCES factory_control."order" (code) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: purchases_uq | type: CONSTRAINT --
-- ALTER TABLE factory_control.purchases DROP CONSTRAINT IF EXISTS purchases_uq CASCADE;
ALTER TABLE factory_control.purchases ADD CONSTRAINT purchases_uq UNIQUE (code_order);
-- ddl-end --

-- object: factory_control.equipment | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.equipment CASCADE;
CREATE TABLE factory_control.equipment (
	code_pk_department varchar(4),
	code_pk_project uuid
);
-- ddl-end --
ALTER TABLE factory_control.equipment OWNER TO postgres;
-- ddl-end --

-- object: department_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.equipment DROP CONSTRAINT IF EXISTS department_fk CASCADE;
ALTER TABLE factory_control.equipment ADD CONSTRAINT department_fk FOREIGN KEY (code_pk_department)
REFERENCES factory_control.department (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: project_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.person DROP CONSTRAINT IF EXISTS project_fk CASCADE;
ALTER TABLE factory_control.person ADD CONSTRAINT project_fk FOREIGN KEY (code_pk_project)
REFERENCES factory_control.project (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: factory_control.sale | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.sale CASCADE;
CREATE TABLE factory_control.sale (
	id_pk bigint NOT NULL,
	code_pk_department varchar(4),
	code_order uuid,
	CONSTRAINT sale_id_pk PRIMARY KEY (id_pk)

);
-- ddl-end --
ALTER TABLE factory_control.sale OWNER TO postgres;
-- ddl-end --

-- object: department_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.sale DROP CONSTRAINT IF EXISTS department_fk CASCADE;
ALTER TABLE factory_control.sale ADD CONSTRAINT department_fk FOREIGN KEY (code_pk_department)
REFERENCES factory_control.department (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: factory_control.product | type: TABLE --
-- DROP TABLE IF EXISTS factory_control.product CASCADE;
CREATE TABLE factory_control.product (
	code_pk_department varchar(4),
	id_pk_sale bigint
);
-- ddl-end --
ALTER TABLE factory_control.product OWNER TO postgres;
-- ddl-end --

-- object: department_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.product DROP CONSTRAINT IF EXISTS department_fk CASCADE;
ALTER TABLE factory_control.product ADD CONSTRAINT department_fk FOREIGN KEY (code_pk_department)
REFERENCES factory_control.department (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: sale_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.product DROP CONSTRAINT IF EXISTS sale_fk CASCADE;
ALTER TABLE factory_control.product ADD CONSTRAINT sale_fk FOREIGN KEY (id_pk_sale)
REFERENCES factory_control.sale (id_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: project_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.equipment DROP CONSTRAINT IF EXISTS project_fk CASCADE;
ALTER TABLE factory_control.equipment ADD CONSTRAINT project_fk FOREIGN KEY (code_pk_project)
REFERENCES factory_control.project (code_pk) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: order_fk | type: CONSTRAINT --
-- ALTER TABLE factory_control.sale DROP CONSTRAINT IF EXISTS order_fk CASCADE;
ALTER TABLE factory_control.sale ADD CONSTRAINT order_fk FOREIGN KEY (code_order)
REFERENCES factory_control."order" (code) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: sale_uq | type: CONSTRAINT --
-- ALTER TABLE factory_control.sale DROP CONSTRAINT IF EXISTS sale_uq CASCADE;
ALTER TABLE factory_control.sale ADD CONSTRAINT sale_uq UNIQUE (code_order);
-- ddl-end --


