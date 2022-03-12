def get_date_summary(cur):
    cur.execute(
        """
        select
            opstime::date as opsdate
            ,sum(value) as sum_value
        from
            sample_date_summary
        group by
            opstime::date
        order by
            opsdate
        ;
        """
    )
    rows = cur.fetchall()
    return rows
