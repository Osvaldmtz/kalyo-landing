# -*- coding: utf-8 -*-
"""Articles 2-7 specs appended to ARTICLES in generate_7_seo_bodies.py"""


def extend_articles(ARTICLES, p):
    from mk_batch7_a2_a7 import articles

    ARTICLES.extend(articles(p))
