PGDMP      +                |         	   Semillero    16.3    16.3 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    17155 	   Semillero    DATABASE     ~   CREATE DATABASE "Semillero" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "Semillero";
                postgres    false                        2615    17157 
   hack3rlabs    SCHEMA        CREATE SCHEMA hack3rlabs;
    DROP SCHEMA hack3rlabs;
                postgres    false            v           1247    17203    change_type_enum    TYPE     [   CREATE TYPE hack3rlabs.change_type_enum AS ENUM (
    'ADD',
    'DELETE',
    'UPDATE'
);
 '   DROP TYPE hack3rlabs.change_type_enum;
    
   hack3rlabs          postgres    false    5                       1255    17427    log_cursos_delete()    FUNCTION       CREATE FUNCTION hack3rlabs.log_cursos_delete() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), OLD.creador_id, 'cursos', 'DELETE', OLD.idcursos, json_build_object(
    'nombre_curso', OLD.nombre_curso,
    'fechainicial_curso', OLD.fechainicial_curso,
    'fechafina_curso', OLD.fechafina_curso,
    'link_curso', OLD.link_curso,
    'descripcion_curso', OLD.descripcion_curso
  ));
  RETURN OLD;
END;
$$;
 .   DROP FUNCTION hack3rlabs.log_cursos_delete();
    
   hack3rlabs          postgres    false    5                       1255    17425    log_cursos_insert()    FUNCTION       CREATE FUNCTION hack3rlabs.log_cursos_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), NEW.creador_id, 'cursos', 'ADD', NEW.idcursos, json_build_object(
    'nombre_curso', NEW.nombre_curso,
    'fechainicial_curso', NEW.fechainicial_curso,
    'fechafina_curso', NEW.fechafina_curso,
    'link_curso', NEW.link_curso,
    'descripcion_curso', NEW.descripcion_curso
  ));
  RETURN NEW;
END;
$$;
 .   DROP FUNCTION hack3rlabs.log_cursos_insert();
    
   hack3rlabs          postgres    false    5                       1255    17426    log_cursos_update()    FUNCTION       CREATE FUNCTION hack3rlabs.log_cursos_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), NEW.creador_id, 'cursos', 'UPDATE', NEW.idcursos, json_build_object(
    'nombre_curso', NEW.nombre_curso,
    'fechainicial_curso', NEW.fechainicial_curso,
    'fechafina_curso', NEW.fechafina_curso,
    'link_curso', NEW.link_curso,
    'descripcion_curso', NEW.descripcion_curso
  ));
  RETURN NEW;
END;
$$;
 .   DROP FUNCTION hack3rlabs.log_cursos_update();
    
   hack3rlabs          postgres    false    5                       1255    17433    log_integrantes_delete()    FUNCTION     J  CREATE FUNCTION hack3rlabs.log_integrantes_delete() RETURNS trigger
    LANGUAGE plpgsql
    AS $_$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), OLD.creador_id, 'integrantes', 'DELETE', OLD.idintegrantes, json_build_object(
    'nombre_integrante', OLD.nombre_integrante,
    'semestre', OLD.semestre,
    'correo', OLD.correo,
    'link_git', OLD.link_git,
    'old_estado', OLD.estado,
    'new_estado', NEW.estado,
    'imagen', substring(OLD.imagen from '/([^/]+)/?$')
  ));
  RETURN OLD;
END;
$_$;
 3   DROP FUNCTION hack3rlabs.log_integrantes_delete();
    
   hack3rlabs          postgres    false    5                       1255    17431    log_integrantes_insert()    FUNCTION     %  CREATE FUNCTION hack3rlabs.log_integrantes_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $_$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), NEW.creador_id, 'integrantes', 'ADD', NEW.idintegrantes, json_build_object(
    'nombre_integrante', NEW.nombre_integrante,
    'semestre', NEW.semestre,
    'correo', NEW.correo,
    'link_git', NEW.link_git,
    'estado', NEW.estado,
    'imagen', substring(NEW.imagen from '/([^/]+)/?$')
  ));
  RETURN NEW;
END;
$_$;
 3   DROP FUNCTION hack3rlabs.log_integrantes_insert();
    
   hack3rlabs          postgres    false    5                       1255    17432    log_integrantes_update()    FUNCTION     J  CREATE FUNCTION hack3rlabs.log_integrantes_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $_$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), NEW.creador_id, 'integrantes', 'UPDATE', NEW.idintegrantes, json_build_object(
    'nombre_integrante', NEW.nombre_integrante,
    'semestre', NEW.semestre,
    'correo', NEW.correo,
    'link_git', NEW.link_git,
    'old_estado', OLD.estado,
    'new_estado', NEW.estado,
    'imagen', substring(NEW.imagen from '/([^/]+)/?$')
  ));
  RETURN NEW;
END;
$_$;
 3   DROP FUNCTION hack3rlabs.log_integrantes_update();
    
   hack3rlabs          postgres    false    5            
           1255    17439    log_noticias_delete()    FUNCTION     �  CREATE FUNCTION hack3rlabs.log_noticias_delete() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), OLD.creador_id, 'noticias', 'DELETE', OLD.idnoticia, json_build_object(
    'nombre_noticia', OLD.nombre_noticia,
    'fecha_noticia', OLD.fecha_noticia,
    'link_noticia', OLD.link_noticia,
    'description_noticia', OLD.description_noticia
  ));
  RETURN OLD;
END;
$$;
 0   DROP FUNCTION hack3rlabs.log_noticias_delete();
    
   hack3rlabs          postgres    false    5            �            1255    17437    log_noticias_insert()    FUNCTION     �  CREATE FUNCTION hack3rlabs.log_noticias_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), NEW.creador_id, 'noticias', 'ADD', NEW.idnoticia, json_build_object(
    'nombre_noticia', NEW.nombre_noticia,
    'fecha_noticia', NEW.fecha_noticia,
    'link_noticia', NEW.link_noticia,
    'description_noticia', NEW.description_noticia
  ));
  RETURN NEW;
END;
$$;
 0   DROP FUNCTION hack3rlabs.log_noticias_insert();
    
   hack3rlabs          postgres    false    5            	           1255    17438    log_noticias_update()    FUNCTION     �  CREATE FUNCTION hack3rlabs.log_noticias_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), NEW.creador_id, 'noticias', 'UPDATE', NEW.idnoticia, json_build_object(
    'nombre_noticia', NEW.nombre_noticia,
    'fecha_noticia', NEW.fecha_noticia,
    'link_noticia', NEW.link_noticia,
    'description_noticia', NEW.description_noticia
  ));
  RETURN NEW;
END;
$$;
 0   DROP FUNCTION hack3rlabs.log_noticias_update();
    
   hack3rlabs          postgres    false    5            �            1255    17421    log_proyectos_delete()    FUNCTION     @  CREATE FUNCTION hack3rlabs.log_proyectos_delete() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), OLD.creador_id, 'proyectos', 'DELETE', OLD.idproyectos, json_build_object(
    'Nombre_Proyecto', OLD.Nombre_Proyecto,
    'Intengrantes_Proyecto', OLD.Intengrantes_Proyecto,
    'Fecha_Proyecto', OLD.Fecha_Proyecto,
    'Link_Proyecto', OLD.Link_Proyecto,
    'Description_Proyecto', OLD.Description_Proyecto
  ));
  RETURN OLD;
END;
$$;
 1   DROP FUNCTION hack3rlabs.log_proyectos_delete();
    
   hack3rlabs          postgres    false    5            �            1255    17419    log_proyectos_insert()    FUNCTION     =  CREATE FUNCTION hack3rlabs.log_proyectos_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), NEW.creador_id, 'proyectos', 'ADD', NEW.idproyectos, json_build_object(
    'Nombre_Proyecto', NEW.Nombre_Proyecto,
    'Intengrantes_Proyecto', NEW.Intengrantes_Proyecto,
    'Fecha_Proyecto', NEW.Fecha_Proyecto,
    'Link_Proyecto', NEW.Link_Proyecto,
    'Description_Proyecto', NEW.Description_Proyecto
  ));
  RETURN NEW;
END;
$$;
 1   DROP FUNCTION hack3rlabs.log_proyectos_insert();
    
   hack3rlabs          postgres    false    5            �            1255    17420    log_proyectos_update()    FUNCTION     @  CREATE FUNCTION hack3rlabs.log_proyectos_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  INSERT INTO audit_log (timestamp, user_id, table_name, change_type, affected_record_id, modified_data)
  VALUES (NOW(), NEW.creador_id, 'proyectos', 'UPDATE', NEW.idproyectos, json_build_object(
    'Nombre_Proyecto', NEW.Nombre_Proyecto,
    'Intengrantes_Proyecto', NEW.Intengrantes_Proyecto,
    'Fecha_Proyecto', NEW.Fecha_Proyecto,
    'Link_Proyecto', NEW.Link_Proyecto,
    'Description_Proyecto', NEW.Description_Proyecto
  ));
  RETURN NEW;
END;
$$;
 1   DROP FUNCTION hack3rlabs.log_proyectos_update();
    
   hack3rlabs          postgres    false    5            �            1259    17210 	   audit_log    TABLE     /  CREATE TABLE hack3rlabs.audit_log (
    id integer NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    table_name character varying(255) NOT NULL,
    change_type hack3rlabs.change_type_enum NOT NULL,
    affected_record_id integer,
    modified_data jsonb
);
 !   DROP TABLE hack3rlabs.audit_log;
    
   hack3rlabs         heap    postgres    false    886    5            �            1259    17209    audit_log_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.audit_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE hack3rlabs.audit_log_id_seq;
    
   hack3rlabs          postgres    false    218    5            �           0    0    audit_log_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE hack3rlabs.audit_log_id_seq OWNED BY hack3rlabs.audit_log.id;
       
   hack3rlabs          postgres    false    217            �            1259    17224 
   auth_group    TABLE     j   CREATE TABLE hack3rlabs.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
 "   DROP TABLE hack3rlabs.auth_group;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17223    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE hack3rlabs.auth_group_id_seq;
    
   hack3rlabs          postgres    false    5    220            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE hack3rlabs.auth_group_id_seq OWNED BY hack3rlabs.auth_group.id;
       
   hack3rlabs          postgres    false    219            �            1259    17256    auth_group_permissions    TABLE     �   CREATE TABLE hack3rlabs.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE hack3rlabs.auth_group_permissions;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17255    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE hack3rlabs.auth_group_permissions_id_seq;
    
   hack3rlabs          postgres    false    5    226            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE hack3rlabs.auth_group_permissions_id_seq OWNED BY hack3rlabs.auth_group_permissions.id;
       
   hack3rlabs          postgres    false    225            �            1259    17242    auth_permission    TABLE     �   CREATE TABLE hack3rlabs.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 '   DROP TABLE hack3rlabs.auth_permission;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17241    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE hack3rlabs.auth_permission_id_seq;
    
   hack3rlabs          postgres    false    224    5            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE hack3rlabs.auth_permission_id_seq OWNED BY hack3rlabs.auth_permission.id;
       
   hack3rlabs          postgres    false    223            �            1259    17194 	   auth_user    TABLE     �  CREATE TABLE hack3rlabs.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp without time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp without time zone NOT NULL
);
 !   DROP TABLE hack3rlabs.auth_user;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17276    auth_user_groups    TABLE     �   CREATE TABLE hack3rlabs.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 (   DROP TABLE hack3rlabs.auth_user_groups;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17275    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE hack3rlabs.auth_user_groups_id_seq;
    
   hack3rlabs          postgres    false    5    228            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE hack3rlabs.auth_user_groups_id_seq OWNED BY hack3rlabs.auth_user_groups.id;
       
   hack3rlabs          postgres    false    227            �            1259    17193    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE hack3rlabs.auth_user_id_seq;
    
   hack3rlabs          postgres    false    5    216            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE hack3rlabs.auth_user_id_seq OWNED BY hack3rlabs.auth_user.id;
       
   hack3rlabs          postgres    false    215            �            1259    17295    auth_user_user_permissions    TABLE     �   CREATE TABLE hack3rlabs.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 2   DROP TABLE hack3rlabs.auth_user_user_permissions;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17294 !   auth_user_user_permissions_id_seq    SEQUENCE     �   ALTER TABLE hack3rlabs.auth_user_user_permissions ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hack3rlabs.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
         
   hack3rlabs          postgres    false    230    5            �            1259    17447    authtoken_token    TABLE     �   CREATE TABLE hack3rlabs.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);
 '   DROP TABLE hack3rlabs.authtoken_token;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17326    cursos    TABLE     s  CREATE TABLE hack3rlabs.cursos (
    idcursos integer NOT NULL,
    nombre_curso character varying(120) NOT NULL,
    fechainicial_curso timestamp without time zone NOT NULL,
    fechafina_curso timestamp without time zone NOT NULL,
    link_curso character varying(200) NOT NULL,
    descripcion_curso character varying(450) NOT NULL,
    creador_id integer NOT NULL
);
    DROP TABLE hack3rlabs.cursos;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17325    cursos_idcursos_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.cursos_idcursos_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE hack3rlabs.cursos_idcursos_seq;
    
   hack3rlabs          postgres    false    232    5            �           0    0    cursos_idcursos_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE hack3rlabs.cursos_idcursos_seq OWNED BY hack3rlabs.cursos.idcursos;
       
   hack3rlabs          postgres    false    231            �            1259    17340    django_admin_log    TABLE     �  CREATE TABLE hack3rlabs.django_admin_log (
    id integer NOT NULL,
    action_time timestamp(6) without time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 (   DROP TABLE hack3rlabs.django_admin_log;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17339    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE hack3rlabs.django_admin_log_id_seq;
    
   hack3rlabs          postgres    false    234    5            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE hack3rlabs.django_admin_log_id_seq OWNED BY hack3rlabs.django_admin_log.id;
       
   hack3rlabs          postgres    false    233            �            1259    17233    django_content_type    TABLE     �   CREATE TABLE hack3rlabs.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 +   DROP TABLE hack3rlabs.django_content_type;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17232    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE hack3rlabs.django_content_type_id_seq;
    
   hack3rlabs          postgres    false    222    5            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE hack3rlabs.django_content_type_id_seq OWNED BY hack3rlabs.django_content_type.id;
       
   hack3rlabs          postgres    false    221            �            1259    17360    django_migrations    TABLE     �   CREATE TABLE hack3rlabs.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp without time zone NOT NULL
);
 )   DROP TABLE hack3rlabs.django_migrations;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17359    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE hack3rlabs.django_migrations_id_seq;
    
   hack3rlabs          postgres    false    236    5            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE hack3rlabs.django_migrations_id_seq OWNED BY hack3rlabs.django_migrations.id;
       
   hack3rlabs          postgres    false    235            �            1259    17460    django_session    TABLE     �   CREATE TABLE hack3rlabs.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 &   DROP TABLE hack3rlabs.django_session;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17377    integrantes    TABLE     Y  CREATE TABLE hack3rlabs.integrantes (
    idintegrantes integer NOT NULL,
    nombre_integrante character varying(120) NOT NULL,
    semestre character varying(50) NOT NULL,
    correo character varying(100) NOT NULL,
    link_git character varying(200) NOT NULL,
    imagen text NOT NULL,
    creador_id integer NOT NULL,
    estado boolean
);
 #   DROP TABLE hack3rlabs.integrantes;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17376    integrantes_idintegrantes_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.integrantes_idintegrantes_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE hack3rlabs.integrantes_idintegrantes_seq;
    
   hack3rlabs          postgres    false    5    238            �           0    0    integrantes_idintegrantes_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE hack3rlabs.integrantes_idintegrantes_seq OWNED BY hack3rlabs.integrantes.idintegrantes;
       
   hack3rlabs          postgres    false    237            �            1259    17392    noticias    TABLE     =  CREATE TABLE hack3rlabs.noticias (
    idnoticia integer NOT NULL,
    nombre_noticia character varying(600) NOT NULL,
    fecha_noticia timestamp without time zone NOT NULL,
    link_noticia character varying(250) NOT NULL,
    description_noticia character varying(450) NOT NULL,
    creador_id integer NOT NULL
);
     DROP TABLE hack3rlabs.noticias;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17391    noticias_idnoticia_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.noticias_idnoticia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE hack3rlabs.noticias_idnoticia_seq;
    
   hack3rlabs          postgres    false    5    240            �           0    0    noticias_idnoticia_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE hack3rlabs.noticias_idnoticia_seq OWNED BY hack3rlabs.noticias.idnoticia;
       
   hack3rlabs          postgres    false    239            �            1259    17406 	   proyectos    TABLE       CREATE TABLE hack3rlabs.proyectos (
    idproyectos integer NOT NULL,
    nombre_proyecto character varying(150) NOT NULL,
    intengrantes_proyecto character varying(450) NOT NULL,
    fecha_proyecto timestamp without time zone NOT NULL,
    link_proyecto character varying(250) NOT NULL,
    description_proyecto character varying(450) NOT NULL,
    creador_id integer NOT NULL
);
 !   DROP TABLE hack3rlabs.proyectos;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17405    proyectos_idproyectos_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.proyectos_idproyectos_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE hack3rlabs.proyectos_idproyectos_seq;
    
   hack3rlabs          postgres    false    242    5            �           0    0    proyectos_idproyectos_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE hack3rlabs.proyectos_idproyectos_seq OWNED BY hack3rlabs.proyectos.idproyectos;
       
   hack3rlabs          postgres    false    241            �            1259    17685    proyectos_integrantes_proyecto    TABLE     �   CREATE TABLE hack3rlabs.proyectos_integrantes_proyecto (
    id integer NOT NULL,
    proyectos_id integer NOT NULL,
    integrantes_id integer NOT NULL
);
 6   DROP TABLE hack3rlabs.proyectos_integrantes_proyecto;
    
   hack3rlabs         heap    postgres    false    5            �            1259    17684 %   proyectos_integrantes_proyecto_id_seq    SEQUENCE     �   CREATE SEQUENCE hack3rlabs.proyectos_integrantes_proyecto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 @   DROP SEQUENCE hack3rlabs.proyectos_integrantes_proyecto_id_seq;
    
   hack3rlabs          postgres    false    5    246            �           0    0 %   proyectos_integrantes_proyecto_id_seq    SEQUENCE OWNED BY     w   ALTER SEQUENCE hack3rlabs.proyectos_integrantes_proyecto_id_seq OWNED BY hack3rlabs.proyectos_integrantes_proyecto.id;
       
   hack3rlabs          postgres    false    245            �           2604    17213    audit_log id    DEFAULT     t   ALTER TABLE ONLY hack3rlabs.audit_log ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.audit_log_id_seq'::regclass);
 ?   ALTER TABLE hack3rlabs.audit_log ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    218    217    218            �           2604    17227    auth_group id    DEFAULT     v   ALTER TABLE ONLY hack3rlabs.auth_group ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.auth_group_id_seq'::regclass);
 @   ALTER TABLE hack3rlabs.auth_group ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    219    220    220            �           2604    17259    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.auth_group_permissions_id_seq'::regclass);
 L   ALTER TABLE hack3rlabs.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    225    226    226            �           2604    17245    auth_permission id    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.auth_permission ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.auth_permission_id_seq'::regclass);
 E   ALTER TABLE hack3rlabs.auth_permission ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    224    223    224            �           2604    17197    auth_user id    DEFAULT     t   ALTER TABLE ONLY hack3rlabs.auth_user ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.auth_user_id_seq'::regclass);
 ?   ALTER TABLE hack3rlabs.auth_user ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    215    216    216            �           2604    17279    auth_user_groups id    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.auth_user_groups_id_seq'::regclass);
 F   ALTER TABLE hack3rlabs.auth_user_groups ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    227    228    228            �           2604    17329    cursos idcursos    DEFAULT     z   ALTER TABLE ONLY hack3rlabs.cursos ALTER COLUMN idcursos SET DEFAULT nextval('hack3rlabs.cursos_idcursos_seq'::regclass);
 B   ALTER TABLE hack3rlabs.cursos ALTER COLUMN idcursos DROP DEFAULT;
    
   hack3rlabs          postgres    false    232    231    232            �           2604    17343    django_admin_log id    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.django_admin_log ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.django_admin_log_id_seq'::regclass);
 F   ALTER TABLE hack3rlabs.django_admin_log ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    233    234    234            �           2604    17236    django_content_type id    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.django_content_type ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.django_content_type_id_seq'::regclass);
 I   ALTER TABLE hack3rlabs.django_content_type ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    222    221    222            �           2604    17363    django_migrations id    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.django_migrations ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.django_migrations_id_seq'::regclass);
 G   ALTER TABLE hack3rlabs.django_migrations ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    236    235    236            �           2604    17380    integrantes idintegrantes    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.integrantes ALTER COLUMN idintegrantes SET DEFAULT nextval('hack3rlabs.integrantes_idintegrantes_seq'::regclass);
 L   ALTER TABLE hack3rlabs.integrantes ALTER COLUMN idintegrantes DROP DEFAULT;
    
   hack3rlabs          postgres    false    237    238    238            �           2604    17395    noticias idnoticia    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.noticias ALTER COLUMN idnoticia SET DEFAULT nextval('hack3rlabs.noticias_idnoticia_seq'::regclass);
 E   ALTER TABLE hack3rlabs.noticias ALTER COLUMN idnoticia DROP DEFAULT;
    
   hack3rlabs          postgres    false    239    240    240            �           2604    17409    proyectos idproyectos    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.proyectos ALTER COLUMN idproyectos SET DEFAULT nextval('hack3rlabs.proyectos_idproyectos_seq'::regclass);
 H   ALTER TABLE hack3rlabs.proyectos ALTER COLUMN idproyectos DROP DEFAULT;
    
   hack3rlabs          postgres    false    242    241    242            �           2604    17688 !   proyectos_integrantes_proyecto id    DEFAULT     �   ALTER TABLE ONLY hack3rlabs.proyectos_integrantes_proyecto ALTER COLUMN id SET DEFAULT nextval('hack3rlabs.proyectos_integrantes_proyecto_id_seq'::regclass);
 T   ALTER TABLE hack3rlabs.proyectos_integrantes_proyecto ALTER COLUMN id DROP DEFAULT;
    
   hack3rlabs          postgres    false    245    246    246            �          0    17210 	   audit_log 
   TABLE DATA           }   COPY hack3rlabs.audit_log (id, "timestamp", user_id, table_name, change_type, affected_record_id, modified_data) FROM stdin;
 
   hack3rlabs          postgres    false    218   �       �          0    17224 
   auth_group 
   TABLE DATA           2   COPY hack3rlabs.auth_group (id, name) FROM stdin;
 
   hack3rlabs          postgres    false    220   8�       �          0    17256    auth_group_permissions 
   TABLE DATA           Q   COPY hack3rlabs.auth_group_permissions (id, group_id, permission_id) FROM stdin;
 
   hack3rlabs          postgres    false    226   e�       �          0    17242    auth_permission 
   TABLE DATA           R   COPY hack3rlabs.auth_permission (id, name, content_type_id, codename) FROM stdin;
 
   hack3rlabs          postgres    false    224   ��       �          0    17194 	   auth_user 
   TABLE DATA           �   COPY hack3rlabs.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
 
   hack3rlabs          postgres    false    216   ]�       �          0    17276    auth_user_groups 
   TABLE DATA           E   COPY hack3rlabs.auth_user_groups (id, user_id, group_id) FROM stdin;
 
   hack3rlabs          postgres    false    228   ��       �          0    17295    auth_user_user_permissions 
   TABLE DATA           T   COPY hack3rlabs.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
 
   hack3rlabs          postgres    false    230   ��       �          0    17447    authtoken_token 
   TABLE DATA           D   COPY hack3rlabs.authtoken_token (key, created, user_id) FROM stdin;
 
   hack3rlabs          postgres    false    243   �       �          0    17326    cursos 
   TABLE DATA           �   COPY hack3rlabs.cursos (idcursos, nombre_curso, fechainicial_curso, fechafina_curso, link_curso, descripcion_curso, creador_id) FROM stdin;
 
   hack3rlabs          postgres    false    232   r�       �          0    17340    django_admin_log 
   TABLE DATA           �   COPY hack3rlabs.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
 
   hack3rlabs          postgres    false    234   ��       �          0    17233    django_content_type 
   TABLE DATA           G   COPY hack3rlabs.django_content_type (id, app_label, model) FROM stdin;
 
   hack3rlabs          postgres    false    222   ��       �          0    17360    django_migrations 
   TABLE DATA           G   COPY hack3rlabs.django_migrations (id, app, name, applied) FROM stdin;
 
   hack3rlabs          postgres    false    236   `�       �          0    17460    django_session 
   TABLE DATA           T   COPY hack3rlabs.django_session (session_key, session_data, expire_date) FROM stdin;
 
   hack3rlabs          postgres    false    244   }�       �          0    17377    integrantes 
   TABLE DATA           �   COPY hack3rlabs.integrantes (idintegrantes, nombre_integrante, semestre, correo, link_git, imagen, creador_id, estado) FROM stdin;
 
   hack3rlabs          postgres    false    238   ��       �          0    17392    noticias 
   TABLE DATA              COPY hack3rlabs.noticias (idnoticia, nombre_noticia, fecha_noticia, link_noticia, description_noticia, creador_id) FROM stdin;
 
   hack3rlabs          postgres    false    240   	�       �          0    17406 	   proyectos 
   TABLE DATA           �   COPY hack3rlabs.proyectos (idproyectos, nombre_proyecto, intengrantes_proyecto, fecha_proyecto, link_proyecto, description_proyecto, creador_id) FROM stdin;
 
   hack3rlabs          postgres    false    242   &�       �          0    17685    proyectos_integrantes_proyecto 
   TABLE DATA           ^   COPY hack3rlabs.proyectos_integrantes_proyecto (id, proyectos_id, integrantes_id) FROM stdin;
 
   hack3rlabs          postgres    false    246   C�       �           0    0    audit_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('hack3rlabs.audit_log_id_seq', 1200, false);
       
   hack3rlabs          postgres    false    217            �           0    0    auth_group_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('hack3rlabs.auth_group_id_seq', 2, true);
       
   hack3rlabs          postgres    false    219            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('hack3rlabs.auth_group_permissions_id_seq', 640, true);
       
   hack3rlabs          postgres    false    225            �           0    0    auth_permission_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('hack3rlabs.auth_permission_id_seq', 32, true);
       
   hack3rlabs          postgres    false    223            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('hack3rlabs.auth_user_groups_id_seq', 2, true);
       
   hack3rlabs          postgres    false    227            �           0    0    auth_user_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('hack3rlabs.auth_user_id_seq', 3, true);
       
   hack3rlabs          postgres    false    215            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     T   SELECT pg_catalog.setval('hack3rlabs.auth_user_user_permissions_id_seq', 1, false);
       
   hack3rlabs          postgres    false    229            �           0    0    cursos_idcursos_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('hack3rlabs.cursos_idcursos_seq', 5200, false);
       
   hack3rlabs          postgres    false    231            �           0    0    django_admin_log_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('hack3rlabs.django_admin_log_id_seq', 8, true);
       
   hack3rlabs          postgres    false    233            �           0    0    django_content_type_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('hack3rlabs.django_content_type_id_seq', 13, true);
       
   hack3rlabs          postgres    false    221            �           0    0    django_migrations_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('hack3rlabs.django_migrations_id_seq', 25, true);
       
   hack3rlabs          postgres    false    235            �           0    0    integrantes_idintegrantes_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('hack3rlabs.integrantes_idintegrantes_seq', 3200, false);
       
   hack3rlabs          postgres    false    237            �           0    0    noticias_idnoticia_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('hack3rlabs.noticias_idnoticia_seq', 7200, false);
       
   hack3rlabs          postgres    false    239            �           0    0    proyectos_idproyectos_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('hack3rlabs.proyectos_idproyectos_seq', 9201, true);
       
   hack3rlabs          postgres    false    241            �           0    0 %   proyectos_integrantes_proyecto_id_seq    SEQUENCE SET     X   SELECT pg_catalog.setval('hack3rlabs.proyectos_integrantes_proyecto_id_seq', 1, false);
       
   hack3rlabs          postgres    false    245            �           2606    17217    audit_log audit_log_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY hack3rlabs.audit_log
    ADD CONSTRAINT audit_log_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY hack3rlabs.audit_log DROP CONSTRAINT audit_log_pkey;
    
   hack3rlabs            postgres    false    218            �           2606    17446    auth_group auth_group_name_key 
   CONSTRAINT     ]   ALTER TABLE ONLY hack3rlabs.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 L   ALTER TABLE ONLY hack3rlabs.auth_group DROP CONSTRAINT auth_group_name_key;
    
   hack3rlabs            postgres    false    220            �           2606    17263 I   auth_group_permissions auth_group_permissions_group_id_permission_id_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_uniq UNIQUE (group_id, permission_id);
 w   ALTER TABLE ONLY hack3rlabs.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_uniq;
    
   hack3rlabs            postgres    false    226    226            �           2606    17261 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY hack3rlabs.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 `   ALTER TABLE ONLY hack3rlabs.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
    
   hack3rlabs            postgres    false    226            �           2606    17229    auth_group auth_group_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY hack3rlabs.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY hack3rlabs.auth_group DROP CONSTRAINT auth_group_pkey;
    
   hack3rlabs            postgres    false    220            �           2606    17249 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 t   ALTER TABLE ONLY hack3rlabs.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
    
   hack3rlabs            postgres    false    224    224            �           2606    17247 $   auth_permission auth_permission_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY hack3rlabs.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY hack3rlabs.auth_permission DROP CONSTRAINT auth_permission_pkey;
    
   hack3rlabs            postgres    false    224            �           2606    17281 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY hack3rlabs.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY hack3rlabs.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
    
   hack3rlabs            postgres    false    228            �           2606    17283 7   auth_user_groups auth_user_groups_user_id_group_id_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_uniq UNIQUE (user_id, group_id);
 e   ALTER TABLE ONLY hack3rlabs.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_uniq;
    
   hack3rlabs            postgres    false    228    228            �           2606    17201    auth_user auth_user_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY hack3rlabs.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY hack3rlabs.auth_user DROP CONSTRAINT auth_user_pkey;
    
   hack3rlabs            postgres    false    216            �           2606    17299 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY hack3rlabs.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 h   ALTER TABLE ONLY hack3rlabs.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
    
   hack3rlabs            postgres    false    230            �           2606    17451 $   authtoken_token authtoken_token_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY hack3rlabs.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);
 R   ALTER TABLE ONLY hack3rlabs.authtoken_token DROP CONSTRAINT authtoken_token_pkey;
    
   hack3rlabs            postgres    false    243            �           2606    17453 +   authtoken_token authtoken_token_user_id_key 
   CONSTRAINT     m   ALTER TABLE ONLY hack3rlabs.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);
 Y   ALTER TABLE ONLY hack3rlabs.authtoken_token DROP CONSTRAINT authtoken_token_user_id_key;
    
   hack3rlabs            postgres    false    243            �           2606    17333    cursos cursos_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY hack3rlabs.cursos
    ADD CONSTRAINT cursos_pkey PRIMARY KEY (idcursos);
 @   ALTER TABLE ONLY hack3rlabs.cursos DROP CONSTRAINT cursos_pkey;
    
   hack3rlabs            postgres    false    232            �           2606    17348 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY hack3rlabs.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY hack3rlabs.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
    
   hack3rlabs            postgres    false    234            �           2606    17240 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 s   ALTER TABLE ONLY hack3rlabs.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
    
   hack3rlabs            postgres    false    222    222            �           2606    17238 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY hack3rlabs.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY hack3rlabs.django_content_type DROP CONSTRAINT django_content_type_pkey;
    
   hack3rlabs            postgres    false    222            �           2606    17367 (   django_migrations django_migrations_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY hack3rlabs.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY hack3rlabs.django_migrations DROP CONSTRAINT django_migrations_pkey;
    
   hack3rlabs            postgres    false    236            �           2606    17466 "   django_session django_session_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY hack3rlabs.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 P   ALTER TABLE ONLY hack3rlabs.django_session DROP CONSTRAINT django_session_pkey;
    
   hack3rlabs            postgres    false    244            �           2606    17384    integrantes integrantes_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY hack3rlabs.integrantes
    ADD CONSTRAINT integrantes_pkey PRIMARY KEY (idintegrantes);
 J   ALTER TABLE ONLY hack3rlabs.integrantes DROP CONSTRAINT integrantes_pkey;
    
   hack3rlabs            postgres    false    238            �           2606    17399    noticias noticias_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY hack3rlabs.noticias
    ADD CONSTRAINT noticias_pkey PRIMARY KEY (idnoticia);
 D   ALTER TABLE ONLY hack3rlabs.noticias DROP CONSTRAINT noticias_pkey;
    
   hack3rlabs            postgres    false    240            �           2606    17690 B   proyectos_integrantes_proyecto proyectos_integrantes_proyecto_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.proyectos_integrantes_proyecto
    ADD CONSTRAINT proyectos_integrantes_proyecto_pkey PRIMARY KEY (id);
 p   ALTER TABLE ONLY hack3rlabs.proyectos_integrantes_proyecto DROP CONSTRAINT proyectos_integrantes_proyecto_pkey;
    
   hack3rlabs            postgres    false    246            �           2606    17413    proyectos proyectos_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY hack3rlabs.proyectos
    ADD CONSTRAINT proyectos_pkey PRIMARY KEY (idproyectos);
 F   ALTER TABLE ONLY hack3rlabs.proyectos DROP CONSTRAINT proyectos_pkey;
    
   hack3rlabs            postgres    false    242            �           2606    17301 K   auth_user_user_permissions user_user_permissions_user_id_permission_id_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_user_user_permissions
    ADD CONSTRAINT user_user_permissions_user_id_permission_id_uniq UNIQUE (user_id, permission_id);
 y   ALTER TABLE ONLY hack3rlabs.auth_user_user_permissions DROP CONSTRAINT user_user_permissions_user_id_permission_id_uniq;
    
   hack3rlabs            postgres    false    230    230            �           1259    17459 !   authtoken_token_key_10f0b77e_like    INDEX     t   CREATE INDEX authtoken_token_key_10f0b77e_like ON hack3rlabs.authtoken_token USING btree (key varchar_pattern_ops);
 9   DROP INDEX hack3rlabs.authtoken_token_key_10f0b77e_like;
    
   hack3rlabs            postgres    false    243            �           1259    17468 #   django_session_expire_date_a5c62663    INDEX     i   CREATE INDEX django_session_expire_date_a5c62663 ON hack3rlabs.django_session USING btree (expire_date);
 ;   DROP INDEX hack3rlabs.django_session_expire_date_a5c62663;
    
   hack3rlabs            postgres    false    244            �           1259    17467 (   django_session_session_key_c0390e0f_like    INDEX     �   CREATE INDEX django_session_session_key_c0390e0f_like ON hack3rlabs.django_session USING btree (session_key varchar_pattern_ops);
 @   DROP INDEX hack3rlabs.django_session_session_key_c0390e0f_like;
    
   hack3rlabs            postgres    false    244                        2620    17430    cursos after_cursos_delete    TRIGGER     �   CREATE TRIGGER after_cursos_delete AFTER DELETE ON hack3rlabs.cursos FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_cursos_delete();
 7   DROP TRIGGER after_cursos_delete ON hack3rlabs.cursos;
    
   hack3rlabs          postgres    false    232    261                       2620    17428    cursos after_cursos_insert    TRIGGER     �   CREATE TRIGGER after_cursos_insert AFTER INSERT ON hack3rlabs.cursos FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_cursos_insert();
 7   DROP TRIGGER after_cursos_insert ON hack3rlabs.cursos;
    
   hack3rlabs          postgres    false    263    232                       2620    17429    cursos after_cursos_update    TRIGGER     �   CREATE TRIGGER after_cursos_update AFTER UPDATE ON hack3rlabs.cursos FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_cursos_update();
 7   DROP TRIGGER after_cursos_update ON hack3rlabs.cursos;
    
   hack3rlabs          postgres    false    264    232                       2620    17436 $   integrantes after_integrantes_delete    TRIGGER     �   CREATE TRIGGER after_integrantes_delete AFTER DELETE ON hack3rlabs.integrantes FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_integrantes_delete();
 A   DROP TRIGGER after_integrantes_delete ON hack3rlabs.integrantes;
    
   hack3rlabs          postgres    false    238    267                       2620    17434 $   integrantes after_integrantes_insert    TRIGGER     �   CREATE TRIGGER after_integrantes_insert AFTER INSERT ON hack3rlabs.integrantes FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_integrantes_insert();
 A   DROP TRIGGER after_integrantes_insert ON hack3rlabs.integrantes;
    
   hack3rlabs          postgres    false    269    238                       2620    17435 $   integrantes after_integrantes_update    TRIGGER     �   CREATE TRIGGER after_integrantes_update AFTER UPDATE ON hack3rlabs.integrantes FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_integrantes_update();
 A   DROP TRIGGER after_integrantes_update ON hack3rlabs.integrantes;
    
   hack3rlabs          postgres    false    268    238                       2620    17442    noticias after_noticias_delete    TRIGGER     �   CREATE TRIGGER after_noticias_delete AFTER DELETE ON hack3rlabs.noticias FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_noticias_delete();
 ;   DROP TRIGGER after_noticias_delete ON hack3rlabs.noticias;
    
   hack3rlabs          postgres    false    266    240                       2620    17440    noticias after_noticias_insert    TRIGGER     �   CREATE TRIGGER after_noticias_insert AFTER INSERT ON hack3rlabs.noticias FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_noticias_insert();
 ;   DROP TRIGGER after_noticias_insert ON hack3rlabs.noticias;
    
   hack3rlabs          postgres    false    254    240                       2620    17441    noticias after_noticias_update    TRIGGER     �   CREATE TRIGGER after_noticias_update AFTER UPDATE ON hack3rlabs.noticias FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_noticias_update();
 ;   DROP TRIGGER after_noticias_update ON hack3rlabs.noticias;
    
   hack3rlabs          postgres    false    265    240            	           2620    17424     proyectos after_proyectos_delete    TRIGGER     �   CREATE TRIGGER after_proyectos_delete AFTER DELETE ON hack3rlabs.proyectos FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_proyectos_delete();
 =   DROP TRIGGER after_proyectos_delete ON hack3rlabs.proyectos;
    
   hack3rlabs          postgres    false    242    249            
           2620    17422     proyectos after_proyectos_insert    TRIGGER     �   CREATE TRIGGER after_proyectos_insert AFTER INSERT ON hack3rlabs.proyectos FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_proyectos_insert();
 =   DROP TRIGGER after_proyectos_insert ON hack3rlabs.proyectos;
    
   hack3rlabs          postgres    false    242    247                       2620    17423     proyectos after_proyectos_update    TRIGGER     �   CREATE TRIGGER after_proyectos_update AFTER UPDATE ON hack3rlabs.proyectos FOR EACH ROW EXECUTE FUNCTION hack3rlabs.log_proyectos_update();
 =   DROP TRIGGER after_proyectos_update ON hack3rlabs.proyectos;
    
   hack3rlabs          postgres    false    248    242            �           2606    17218     audit_log audit_log_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.audit_log
    ADD CONSTRAINT audit_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES hack3rlabs.auth_user(id);
 N   ALTER TABLE ONLY hack3rlabs.audit_log DROP CONSTRAINT audit_log_user_id_fkey;
    
   hack3rlabs          postgres    false    218    4797    216            �           2606    17264 9   auth_group_permissions auth_group_permissions_group_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_fk FOREIGN KEY (group_id) REFERENCES hack3rlabs.auth_group(id);
 g   ALTER TABLE ONLY hack3rlabs.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_fk;
    
   hack3rlabs          postgres    false    4803    226    220            �           2606    17269 >   auth_group_permissions auth_group_permissions_permission_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fk FOREIGN KEY (permission_id) REFERENCES hack3rlabs.auth_permission(id);
 l   ALTER TABLE ONLY hack3rlabs.auth_group_permissions DROP CONSTRAINT auth_group_permissions_permission_id_fk;
    
   hack3rlabs          postgres    false    226    224    4811            �           2606    17250 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES hack3rlabs.django_content_type(id);
 s   ALTER TABLE ONLY hack3rlabs.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
    
   hack3rlabs          postgres    false    224    4807    222            �           2606    17284 -   auth_user_groups auth_user_groups_group_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fk FOREIGN KEY (group_id) REFERENCES hack3rlabs.auth_group(id);
 [   ALTER TABLE ONLY hack3rlabs.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_fk;
    
   hack3rlabs          postgres    false    228    4803    220            �           2606    17289 ,   auth_user_groups auth_user_groups_user_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_fk FOREIGN KEY (user_id) REFERENCES hack3rlabs.auth_user(id);
 Z   ALTER TABLE ONLY hack3rlabs.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_fk;
    
   hack3rlabs          postgres    false    228    216    4797            �           2606    17454 @   authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES hack3rlabs.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY hack3rlabs.authtoken_token DROP CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id;
    
   hack3rlabs          postgres    false    216    243    4797            �           2606    17334    cursos fk_creador_id    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.cursos
    ADD CONSTRAINT fk_creador_id FOREIGN KEY (creador_id) REFERENCES hack3rlabs.auth_user(id);
 B   ALTER TABLE ONLY hack3rlabs.cursos DROP CONSTRAINT fk_creador_id;
    
   hack3rlabs          postgres    false    4797    216    232            �           2606    17385    integrantes fk_creador_id    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.integrantes
    ADD CONSTRAINT fk_creador_id FOREIGN KEY (creador_id) REFERENCES hack3rlabs.auth_user(id);
 G   ALTER TABLE ONLY hack3rlabs.integrantes DROP CONSTRAINT fk_creador_id;
    
   hack3rlabs          postgres    false    216    238    4797            �           2606    17400    noticias fk_creador_id    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.noticias
    ADD CONSTRAINT fk_creador_id FOREIGN KEY (creador_id) REFERENCES hack3rlabs.auth_user(id);
 D   ALTER TABLE ONLY hack3rlabs.noticias DROP CONSTRAINT fk_creador_id;
    
   hack3rlabs          postgres    false    240    4797    216            �           2606    17414    proyectos fk_creador_id    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.proyectos
    ADD CONSTRAINT fk_creador_id FOREIGN KEY (creador_id) REFERENCES hack3rlabs.auth_user(id);
 E   ALTER TABLE ONLY hack3rlabs.proyectos DROP CONSTRAINT fk_creador_id;
    
   hack3rlabs          postgres    false    4797    216    242            �           2606    17349 4   django_admin_log fk_django_admin_log_content_type_id    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.django_admin_log
    ADD CONSTRAINT fk_django_admin_log_content_type_id FOREIGN KEY (content_type_id) REFERENCES hack3rlabs.django_content_type(id);
 b   ALTER TABLE ONLY hack3rlabs.django_admin_log DROP CONSTRAINT fk_django_admin_log_content_type_id;
    
   hack3rlabs          postgres    false    4807    234    222            �           2606    17354 ,   django_admin_log fk_django_admin_log_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.django_admin_log
    ADD CONSTRAINT fk_django_admin_log_user_id FOREIGN KEY (user_id) REFERENCES hack3rlabs.auth_user(id);
 Z   ALTER TABLE ONLY hack3rlabs.django_admin_log DROP CONSTRAINT fk_django_admin_log_user_id;
    
   hack3rlabs          postgres    false    4797    234    216            �           2606    17696 P   proyectos_integrantes_proyecto proyectos_integrantes_proyecto_integrante_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.proyectos_integrantes_proyecto
    ADD CONSTRAINT proyectos_integrantes_proyecto_integrante_id_fkey FOREIGN KEY (integrantes_id) REFERENCES hack3rlabs.integrantes(idintegrantes);
 ~   ALTER TABLE ONLY hack3rlabs.proyectos_integrantes_proyecto DROP CONSTRAINT proyectos_integrantes_proyecto_integrante_id_fkey;
    
   hack3rlabs          postgres    false    4831    246    238            �           2606    17691 N   proyectos_integrantes_proyecto proyectos_integrantes_proyecto_proyecto_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.proyectos_integrantes_proyecto
    ADD CONSTRAINT proyectos_integrantes_proyecto_proyecto_id_fkey FOREIGN KEY (proyectos_id) REFERENCES hack3rlabs.proyectos(idproyectos);
 |   ALTER TABLE ONLY hack3rlabs.proyectos_integrantes_proyecto DROP CONSTRAINT proyectos_integrantes_proyecto_proyecto_id_fkey;
    
   hack3rlabs          postgres    false    242    4835    246            �           2606    17307 A   auth_user_user_permissions user_user_permissions_permission_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_user_user_permissions
    ADD CONSTRAINT user_user_permissions_permission_id_fk FOREIGN KEY (permission_id) REFERENCES hack3rlabs.auth_permission(id);
 o   ALTER TABLE ONLY hack3rlabs.auth_user_user_permissions DROP CONSTRAINT user_user_permissions_permission_id_fk;
    
   hack3rlabs          postgres    false    224    230    4811            �           2606    17302 ;   auth_user_user_permissions user_user_permissions_user_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY hack3rlabs.auth_user_user_permissions
    ADD CONSTRAINT user_user_permissions_user_id_fk FOREIGN KEY (user_id) REFERENCES hack3rlabs.auth_user(id);
 i   ALTER TABLE ONLY hack3rlabs.auth_user_user_permissions DROP CONSTRAINT user_user_permissions_user_id_fk;
    
   hack3rlabs          postgres    false    230    4797    216            �      x������ � �      �      x�3�.ILK�2�tL�������� =:      �   �   x�λ�E1Q�v0[b����c9tap����S��e��N�ՙhw
��B����9d�~����� �D��"IK1ISQ��X���Lkq���2�iP�S�ۃ���ߟI�פ�(�Z�}mʾ˾.�y�e/����6#g      �   R  x�m�An�0E��)8A�$�u��e�
���i���=C��x�X�?�ZuYU��ct�2j9��G�S��Qu�ۚ�
}'��\7�*h|���G���NO���&	���	�nݏ�֋Ѭw�W;���TIj�B�\N��c��	��5��(P�䠉������"���o}���jC �\6�4��c�x�vlX�h�xh��o����i�ZX�w�6"�=��"�� �@�R��,�����zL��Q�\�� �FN�qP�[��,2�hu��nrr��B�gn��)�Md��L&� �/{�,�������X��<��`�O�2� ��h�� ���=      �   d  x�u�KO�@�5��.�q�3�$&j�jc	�}�� } ��BMԳ�9��\"��<���z@��Q��Sf�?:�t9�ă��"����x=$�6P��nu'bnYi�pW��ha�6��K	h爝 p�h*�	%D�%/,�K}b���b4 ����oٲr��r��Q+��hw��3S���B�bY��6y��}ڑdʃ�غ9����y[|˰9 ������(3po)�2������Y��ϓ_�2���˄TE��%�8ŪN1Չ(fw��sN�Q4!l���l����o�������E�-��}*nX�ؘ�+2�1 � aN5L�a���<�^��Z�)��UY��ԋ��      �      x�3�4�4�2�4�4����� <      �      x������ � �      �   K   x����  ��T�t8�Z��$���]N�3�fD�����h����/E�S�W����-�%����VE`7 �HR�      �      x������ � �      �     x���KN1�יST�od;qb�8D�"�T��(��ޝTmił]�����KK��<1[�(����3���j?�Rj���pX�
tˆ	Ѣzj�I�u���u�,�E�(��ґ��i�t�Ƕ�/eן������}7������r�M�c�[�L,6*����x��u�w�״L�Q�J�h,Q[mޥR�)F�<��T�����A�}��G0����ľ�f�N�@$�9��s�Vgʡ%�X]����O�}�������@[��*�b���e�Ij�C_+�P�Y�h�a�k
�      �   �   x�]��
�0��;#���]��t�A�-���74�e��`�q�=�(gt�L�d��SL�s�M���X�+�=�Y*k�S�Lњ�����D�s�\q�s+�%�FI�v2g)+ܞ���dVW�� �Hy����[��ɉ6��Q����� | ��P�      �     x����n� ��S�j�|���.ݚ�bA���_tw��T[�aL�|�9��������<�XPJ�4}36�-�"��+���P5�%pƤ"X�i|߱]p�@Xa�]���_����~4�?%�l����3�do����I"� v$�����yk���}sHU��$�DE�o����u��+���{�@M�F^Bz$#2�ƶ�fp�kb���b��/Ӻ��v�s�f���aW���u�iE SJ��1�#~�^KPh�G@k�8gݤ���]G0�<���R�Sr�K�fj� Y�(�w�����ms��q�h��s1ړ�(���b��V�-W�#�3E�eFœq� �rN�O�>��JJUf�����3C�_燮ۈD
�	��𱘷&�F!RM�Ұ���~�$�dY	�t:]?��2�H����I�)��RP�鳞��sI`C�S�ϲ�x���l�Ew�(F��o���jE�_)+������K�~��������}�nP�����\�"��)��l�����JLf� JB�)���      �   _  x���Kr�0  �u=E/���>;D>J#-�3�A�@�N�v�3t���w�ǇH���X�w9��Q@2�jp����Wv�J����1���
1�֫+��mx�"�M�6��q�iп��:9��ܠ$�s���J̗��C �Y�ER��)->�����1=�y��MÒ�]�5&JmT�`WϫW>����[�M[�?v 8��C[���ŀ��q�\V��a�~��&:�S<|�:i��$�M�1��K@���U C�K�j�,�S{��/o�<2��f4��������������|R8/�-�vNSM�F�#�M�֤���j���3� ˟9�ߢ��b��$���      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     