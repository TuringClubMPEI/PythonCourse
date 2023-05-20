-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 1.0.2
-- PostgreSQL version: 15.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
CREATE DATABASE new_database;
-- ddl-end --


-- object: public."user" | type: TABLE --
-- DROP TABLE IF EXISTS public."user" CASCADE;
CREATE TABLE public."user" (
	id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	name text,
	surname text,
	about text,
	email text,
	age smallint,
	hashed_password text,
	created_date date,
	contact text,
	CONSTRAINT user_id_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public."user" OWNER TO postgres;
-- ddl-end --

-- object: public.achievement | type: TABLE --
-- DROP TABLE IF EXISTS public.achievement CASCADE;
CREATE TABLE public.achievement (
	id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	id_user bigint,
	title text,
	address smallint,
	CONSTRAINT achievement_id_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.achievement OWNER TO postgres;
-- ddl-end --

-- object: public.project | type: TABLE --
-- DROP TABLE IF EXISTS public.project CASCADE;
CREATE TABLE public.project (
	id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	id_user bigint,
	title text,
	participants_number bigint,
	created_date date,
	about text,
	active boolean,
	CONSTRAINT project_id_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.project OWNER TO postgres;
-- ddl-end --

-- object: public.participant | type: TABLE --
-- DROP TABLE IF EXISTS public.participant CASCADE;
CREATE TABLE public.participant (
	id_user bigint,
	id_project bigint

);
-- ddl-end --
ALTER TABLE public.participant OWNER TO postgres;
-- ddl-end --

-- object: public.application | type: TABLE --
-- DROP TABLE IF EXISTS public.application CASCADE;
CREATE TABLE public.application (
	id_user bigint,
	id_project bigint

);
-- ddl-end --
ALTER TABLE public.application OWNER TO postgres;
-- ddl-end --

-- object: user_fk | type: CONSTRAINT --
-- ALTER TABLE public.project DROP CONSTRAINT IF EXISTS user_fk CASCADE;
ALTER TABLE public.project ADD CONSTRAINT user_fk FOREIGN KEY (id_user)
REFERENCES public."user" (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: user_fk | type: CONSTRAINT --
-- ALTER TABLE public.achievement DROP CONSTRAINT IF EXISTS user_fk CASCADE;
ALTER TABLE public.achievement ADD CONSTRAINT user_fk FOREIGN KEY (id_user)
REFERENCES public."user" (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: user_fk | type: CONSTRAINT --
-- ALTER TABLE public.participant DROP CONSTRAINT IF EXISTS user_fk CASCADE;
ALTER TABLE public.participant ADD CONSTRAINT user_fk FOREIGN KEY (id_user)
REFERENCES public."user" (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: user_fk | type: CONSTRAINT --
-- ALTER TABLE public.application DROP CONSTRAINT IF EXISTS user_fk CASCADE;
ALTER TABLE public.application ADD CONSTRAINT user_fk FOREIGN KEY (id_user)
REFERENCES public."user" (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: project_fk | type: CONSTRAINT --
-- ALTER TABLE public.application DROP CONSTRAINT IF EXISTS project_fk CASCADE;
ALTER TABLE public.application ADD CONSTRAINT project_fk FOREIGN KEY (id_project)
REFERENCES public.project (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: project_fk | type: CONSTRAINT --
-- ALTER TABLE public.participant DROP CONSTRAINT IF EXISTS project_fk CASCADE;
ALTER TABLE public.participant ADD CONSTRAINT project_fk FOREIGN KEY (id_project)
REFERENCES public.project (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --


