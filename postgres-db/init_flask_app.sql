SET
    statement_timeout = 0;
SET
    lock_timeout = 0;
SET
    idle_in_transaction_session_timeout = 0;
SET
    client_encoding = 'UTF8';
SET
    standard_conforming_strings = ON;
SELECT
    pg_catalog.set_config('search_path', '', false);
SET
    check_function_bodies = false;
SET
    xmloption = content;
SET
    client_min_messages = warning;
SET
    row_security = off;
SET
    default_tablespace = '';
SET
    default_table_access_method = HEAP;

--
-- Name: users; Type: TABLE; Schema: public; Owner: flask_user
--
CREATE TABLE public.users (
    id integer NOT NULL,
    fname character varying(64),
    lname character varying(64),
    email character varying(128) NOT NULL,
    PASSWORD character varying(512),
    organization character varying(64),
    role character varying(64),
    date_created timestamp without time zone,
    verified boolean,
    vcode character varying(64)
);

ALTER TABLE
    public.users OWNER TO flask_user;

--
-- Name: flask_app_users_id_seq; Type: SEQUENCE; Schema: public; Owner: flask_user
--
CREATE SEQUENCE public.flask_app_users_id_seq AS integer START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;

ALTER TABLE
    public.flask_app_users_id_seq OWNER TO flask_user;

--
-- Name: flask_app_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flask_user
--
ALTER SEQUENCE public.flask_app_users_id_seq OWNED BY public.users.id;

--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: flask_user
--
ALTER TABLE
    ONLY public.users
ALTER COLUMN
    id
SET
    DEFAULT nextval('public.flask_app_users_id_seq' :: regclass);

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: flask_user
--
COPY public.users (
    id,
    fname,
    lname,
    email,
    PASSWORD,
    organization,
    role,
    date_created,
    verified,
    vcode
)
FROM
    stdin;

-- Name: flask_app_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flask_user
--
SELECT
    pg_catalog.setval('public.flask_app_users_id_seq', 15, TRUE);

--
-- Name: users flask_app_users_pkey; Type: CONSTRAINT; Schema: public; Owner: flask_user
--
ALTER TABLE
    ONLY public.users
ADD
    CONSTRAINT flask_app_users_pkey PRIMARY KEY (id);