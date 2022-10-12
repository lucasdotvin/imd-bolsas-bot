INSERT INTO cron.job (schedule, command, nodename, nodeport, database, username, active, jobname)
VALUES (
        '*/30 * * * *',
        '
                select content::json->''status''
                from http((
                ''GET'',
                ''{{ API_BASE_URL }}/share?channel=telegram'',
                ARRAY[http_header(''X-API-KEY'',''{{ API_KEY }}'')],
                NULL,
                NULL
                )::http_request)
        ',
        'localhost',
        '5432',
        'postgres',
        'postgres',
        'true',
        'telegram-share-1-30-minutes'
);

INSERT INTO cron.job (schedule, command, nodename, nodeport, database, username, active, jobname)
VALUES (
        '*/30 * * * *',
        '
                select content::json->''status''
                from http((
                ''GET'',
                ''{{ API_BASE_URL }}/share?channel=twitter'',
                ARRAY[http_header(''X-API-KEY'',''{{ API_KEY }}'')],
                NULL,
                NULL
                )::http_request)
        ',
        'localhost',
        '5432',
        'postgres',
        'postgres',
        'true',
        'twitter-share-1-30-minutes'
);

INSERT INTO cron.job (schedule, command, nodename, nodeport, database, username, active, jobname)
VALUES (
        '*/30 * * * *',
        '
                select content::json->''status''
                from http((
                ''GET'',
                ''{{ API_BASE_URL }}/retrieve?retriever=imd'',
                ARRAY[http_header(''X-API-KEY'',''{{ API_KEY }}'')],
                NULL,
                NULL
                )::http_request)
        ',
        'localhost',
        '5432',
        'postgres',
        'postgres',
        'true',
        'imd-retrieve-1-30-minutes'
);

INSERT INTO cron.job (schedule, command, nodename, nodeport, database, username, active, jobname)
VALUES (
        '*/30 * * * *',
        '
                select content::json->''status''
                from http((
                ''GET'',
                ''{{ API_BASE_URL }}/retrieve?retriever=jerimum'',
                ARRAY[http_header(''X-API-KEY'',''{{ API_KEY }}'')],
                NULL,
                NULL
                )::http_request)
        ',
        'localhost',
        '5432',
        'postgres',
        'postgres',
        'true',
        'jerimum-retrieve-1-30-minutes'
);

INSERT INTO cron.job (schedule, command, nodename, nodeport, database, username, active, jobname)
VALUES (
        '*/30 * * * *',
        '
                select content::json->''status''
                from http((
                ''GET'',
                ''{{ API_BASE_URL }}/retrieve?retriever=lais'',
                ARRAY[http_header(''X-API-KEY'',''{{ API_KEY }}'')],
                NULL,
                NULL
                )::http_request)
        ',
        'localhost',
        '5432',
        'postgres',
        'postgres',
        'true',
        'lais-retrieve-1-30-minutes'
);

INSERT INTO cron.job (schedule, command, nodename, nodeport, database, username, active, jobname)
VALUES (
        '*/15 * * * *',
        '
                select content::json->''status''
                from http((
                ''GET'',
                ''{{ API_BASE_URL }}/health/auth'',
                ARRAY[http_header(''X-API-KEY'',''{{ API_KEY }}'')],
                NULL,
                NULL
                )::http_request)
        ',
        'localhost',
        '5432',
        'postgres',
        'postgres',
        'true',
        'auth-health-check'
);
