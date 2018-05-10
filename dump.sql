--
-- PostgreSQL database dump
--

-- Dumped from database version 9.0.13
-- Dumped by pg_dump version 9.5.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO berntyru;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO berntyru;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO berntyru;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO berntyru;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO berntyru;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO berntyru;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO berntyru;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO berntyru;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO berntyru;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO berntyru;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO berntyru;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO berntyru;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO berntyru;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO berntyru;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO berntyru;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO berntyru;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO berntyru;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: berntyru
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO berntyru;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: berntyru
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO berntyru;

--
-- Name: weather_city; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE weather_city (
    city_id integer NOT NULL,
    name character varying(100) NOT NULL,
    coord_lon numeric(19,10) NOT NULL,
    coord_lat numeric(19,10) NOT NULL,
    country_id character varying(10)
);


ALTER TABLE weather_city OWNER TO berntyru;

--
-- Name: weather_country; Type: TABLE; Schema: public; Owner: berntyru
--

CREATE TABLE weather_country (
    brief character varying(10) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE weather_country OWNER TO berntyru;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add permission	3	add_permission
8	Can change permission	3	change_permission
9	Can delete permission	3	delete_permission
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add country	7	add_country
20	Can change country	7	change_country
21	Can delete country	7	delete_country
22	Can add city	8	add_city
23	Can change city	8	change_city
24	Can delete city	8	delete_city
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('auth_permission_id_seq', 24, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$36000$lCXUGq4E063K$23zrU1ZPFHZCE9gMVo5bDhxvTn+lgfUk/KsLJGKF+1A=	2018-04-25 23:58:01.831933+03	t	admin			leonard.schmidt.com@gmail.com	t	t	2018-04-25 23:44:54.940962+03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	group
3	auth	permission
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	weather	country
8	weather	city
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('django_content_type_id_seq', 8, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-04-25 23:27:43.055925+03
2	auth	0001_initial	2018-04-25 23:27:43.229679+03
3	admin	0001_initial	2018-04-25 23:27:43.285573+03
4	admin	0002_logentry_remove_auto_add	2018-04-25 23:27:43.326643+03
5	contenttypes	0002_remove_content_type_name	2018-04-25 23:27:43.406418+03
6	auth	0002_alter_permission_name_max_length	2018-04-25 23:27:43.677178+03
7	auth	0003_alter_user_email_max_length	2018-04-25 23:27:43.977+03
8	auth	0004_alter_user_username_opts	2018-04-25 23:27:44.012031+03
9	auth	0005_alter_user_last_login_null	2018-04-25 23:27:44.041602+03
10	auth	0006_require_contenttypes_0002	2018-04-25 23:27:44.045692+03
11	auth	0007_alter_validators_add_error_messages	2018-04-25 23:27:44.071335+03
12	auth	0008_alter_user_username_max_length	2018-04-25 23:27:44.590039+03
13	sessions	0001_initial	2018-04-25 23:27:44.609144+03
14	weather	0001_initial	2018-04-26 09:49:25.680556+03
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: berntyru
--

SELECT pg_catalog.setval('django_migrations_id_seq', 14, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
cvccjyryme0uckfnc2u5vf2hhv6g8ce0	MjUxYjkxNzc4NTI0YmE1YmYwMjhkYTI4Njk0YTU3YWZmNTVhNTJmMDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk0NDg1ZDVmOWQxZWE2MGNmZGVhNmQ1NzE4ZjU5ZTZhOTM1MTU0NjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2018-05-09 23:58:01.842566+03
\.


--
-- Data for Name: weather_city; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY weather_city (city_id, name, coord_lon, coord_lat, country_id) FROM stdin;
524901	Moscow	37.6155550000	55.7522200000	RU
499099	Samara	50.1500020000	53.2000010000	RU
\.


--
-- Data for Name: weather_country; Type: TABLE DATA; Schema: public; Owner: berntyru
--

COPY weather_country (brief, name) FROM stdin;
RU	Россия
ES	Испания
JM	Ямайка
AB	Абхазия
AD	Андорра
AU	Австралия
AT	Австрия
AZ	Азербайджан
AL	Албания
DZ	Алжир
AO	Ангола
AG	Антигуа и Барбуда
AR	Аргентина
AM	Армения
AF	Афганистан
BS	Багамские Острова
BD	Бангладеш
BB	Барбадос
BH	Бахрейн
BZ	Белиз
BY	Белоруссия
BE	Бельгия
BJ	Бенин
BG	Болгария
BO	Боливия
BA	Босния и Герцеговина
BW	Ботсвана
BR	Бразилия
BN	Бруней
BF	Буркина-Фасо
BI	Бурунди
BT	Бутан
VU	Вануату
VA	Ватикан
GB	Великобритания
HU	Венгрия
VE	Венесуэла
TL	Восточный Тимор
VN	Вьетнам
GA	Габон
HT	Гаити
GY	Гайана
GM	Гамбия
GH	Гана
GT	Гватемала
GN	Гвинея
GW	Гвинея-Бисау
DE	Германия
HN	Гондурас
PS	Государство Палестина
GD	Гренада
GR	Греция
GE	Грузия
DK	Дания
DJ	Джибути
DM	Доминика
DO	Доминиканская Республика
CD	ДР Конго
EG	Египет
ZM	Замбия
ZW	Зимбабве
IL	Израиль
IN	Индия
ID	Индонезия
JO	Иордания
IQ	Ирак
IR	Иран
IE	Ирландия
IS	Исландия
IT	Италия
YE	Йемен
CV	Кабо-Верде
KZ	Казахстан
KH	Камбоджа
CM	Камерун
CA	Канада
QA	Катар
KE	Кения
CY	Кипр
KG	Киргизия
KI	Кирибати
CN	Китай
KP	КНДР
CO	Колумбия
KM	Коморские Острова
CR	Коста-Рика
CI	Кот-д'Ивуар
CU	Куба
KW	Кувейт
LA	Лаос
LV	Латвия
LS	Лесото
LR	Либерия
LB	Ливан
LY	Ливия
LT	Литва
LI	Лихтенштейн
LU	Люксембург
MU	Маврикий
MR	Мавритания
MG	Мадагаскар
MK	Македония
MW	Малави
MY	Малайзия
ML	Мали
MV	Мальдивские Острова
MT	Мальта
MA	Марокко
MH	Маршалловы Острова
MX	Мексика
MZ	Мозамбик
MD	Молдавия
MC	Монако
MN	Монголия
MM	Мьянма
NA	Намибия
NR	Науру
NP	Непал
NE	Нигер
NG	Нигерия
NL	Нидерланды
NI	Никарагуа
NZ	Новая Зеландия
NO	Норвегия
AE	ОАЭ
OM	Оман
PK	Пакистан
PW	Палау
PA	Панама
PG	Папуа - Новая Гвинея
PY	Парагвай
PE	Перу
PL	Польша
PT	Португалия
CG	Республика Конго
KR	Республика Корея
RW	Руанда
RO	Румыния
SV	Сальвадор
WS	Самоа
SM	Сан-Марино
ST	Сан-Томе и Принсипи
SA	Саудовская Аравия
SZ	Свазиленд
SC	Сейшельские Острова
SN	Сенегал
VC	Сент-Винсент и Гренадины
KN	Сент-Китс и Невис
LC	Сент-Люсия
RS	Сербия
SG	Сингапур
SY	Сирия
SK	Словакия
SI	Словения
SB	Соломоновы Острова
SO	Сомали
SD	Судан
SR	Суринам
US	США
SL	Сьерра-Леоне
TJ	Таджикистан
TH	Таиланд
TZ	Танзания
TG	Того
TO	Тонга
TT	Тринидад и Тобаго
TV	Тувалу
TN	Тунис
TM	Туркмения
TR	Турция
UG	Уганда
UZ	Узбекистан
UA	Украина
UY	Уругвай
FM	Федеративные Штаты Микронезии
FJ	Фиджи
PH	Филиппины
FI	Финляндия
FR	Франция
HR	Хорватия
CF	ЦАР
TD	Чад
ME	Черногория
CZ	Чехия
CL	Чили
CH	Швейцария
SE	Швеция
LK	Шри-Ланка
EC	Эквадор
GQ	Экваториальная Гвинея
ER	Эритрея
EE	Эстония
ET	Эфиопия
ZA	ЮАР
OS	Южная Осетия
SS	Южный Судан
AI	Ангилья
AQ	Антарктика
AS	Восточное (Американское) Самоа
PR	PR
NF	NF
AW	Аруба
BQ	BQ
HK	HK
GG	GG
GU	GU
IM	IM
PN	PN
WF	WF
SJ	SJ
TK	TK
BM	BM
GS	GS
MO	MO
FO	FO
TF	TF
YT	Майотта
GI	GI
GL	GL
PF	PF
PM	PM
SH	SH
GP	GP
NU	NU
SX	SX
EH	EH
TC	TC
KY	KY
MS	MS
NC	NC
GF	GF
CW	CW
MP	MP
CX	CX
VG	VG
__	не определено
JE	JE
TW	TW
VI	VI
RE	RE
FK	FK
MF	MF
MQ	MQ
BL	Сен-Бартелеми
CK	CK
CC	CC
JP	JP
AX	Аландские острова
XK	Косово
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: weather_city_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY weather_city
    ADD CONSTRAINT weather_city_pkey PRIMARY KEY (city_id);


--
-- Name: weather_country_pkey; Type: CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY weather_country
    ADD CONSTRAINT weather_country_pkey PRIMARY KEY (brief);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: weather_city_country_id_6d386839; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX weather_city_country_id_6d386839 ON weather_city USING btree (country_id);


--
-- Name: weather_city_country_id_6d386839_like; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX weather_city_country_id_6d386839_like ON weather_city USING btree (country_id varchar_pattern_ops);


--
-- Name: weather_country_brief_2e9c564f_like; Type: INDEX; Schema: public; Owner: berntyru
--

CREATE INDEX weather_country_brief_2e9c564f_like ON weather_country USING btree (brief varchar_pattern_ops);


--
-- Name: auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: weather_city_country_id_6d386839_fk_weather_country_brief; Type: FK CONSTRAINT; Schema: public; Owner: berntyru
--

ALTER TABLE ONLY weather_city
    ADD CONSTRAINT weather_city_country_id_6d386839_fk_weather_country_brief FOREIGN KEY (country_id) REFERENCES weather_country(brief) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

