3
??b?   ?               @   s?  d Z ddlZddljZejd?Zejd?Z	e	j
? Ze	jZe	jZe	j? Zejd?Zej
? Zejdd?Zejeedddd	?Zej
? Zejed
 dd?ed
< ed
 j? Zed
 dkZeee ?Zed
 ed
 j? kZee d Zee d Z ed j!e"?ed< ed j"j#d?Z$e$j%? Z&ddl'Z'e'j(d? eed
 dk Z)e)j*ddgd?Z+e'j,dee+?d ?Z-e+e-e-d ? d j.d Z/e+d Z0ddl1Z2ej3? Z4e4j3? Z5e5j6dg?j7e2jg?d
  e4j6dg?j7e2jg?d
 Z5dd? Z8e4d j9e8?e4d< e4j
d? dd? Z:e4d j9e:?e4d< e4j
?  e4e4d dk Z;e;j
?  ej<e;dgdgegd?Z=e= e=j>d d.d!dd#d$? ej?d%? d&d'? Z@e4jAj"jB? ZCeCj9e@?e4d(< e4j
?  e4d( jD? ZEeEeEdk ZFeFj>d d/d+d)d,? ej?d-? dS )0zP
We're providing most of the import statements you need for the entire exercise
?    Nzcelebrity_deaths_2016.xlsxZceleb_death?cause_of_deathZcause_id)?subset?left)r   ?rightZhowZleft_onZright_onZageZcoerce)?errors?F   ?namezcause of death?bioZAmerican?2   F)Zinplacer   ?   c             C   s   | j S )N)?month)?date? r   ?1/home/codio/workspace/.guides/secure/solutions.py?	get_month?   s    r   zdate of deathr   ?d   c             C   s   | j S )N)?year)r   r   r   r   ?get_year?   s    r   r   i?  )?index?valuesZaggfuncZbar?   ?   zNumber of Deaths per Month)?kind?figsize?fontsizeZlegend?titlezNumber of deathsc             C   s   | d S )Nr   r   )r	   r   r   r   ?get_nationality?   s    r   ?nationality?   ?   z+Nationality of celebrities who died in 2016)r   r   r   r   zDeath Counts)r   r   )r   r   )G?__doc__ZpandasZpdZmatplotlib.pyplotZpyplotZpltZ	ExcelFileZxlZparseZdf1?headZtop5ZdtypesZ	df_dtypes?shapeZdf_shapeZdrop_duplicatesZdf2r   Z
cause_top5?mergeZdf3Zdf_top5Z
to_numericZmeanZavg_ageZafter70?len?count?minZminageZyoungest_nameZyoungest_causeZastype?str?containsZamerican?sumZcount_americanZrandomZseedZatage50ZdropnaZatage50_not_nullZrandintZrand_intZilocZ
rand_causeZpossible_causesZnumpyZnp?copyZdfZdf_grouped_cause?groupbyZaggr   Zapplyr   Zdf_2016Zpivot_tableZdf_per_monthZplotZylabelr   r	   ?splitr   Zvalue_countsZ	countriesZunlucky_countriesr   r   r   r   ?<module>   st   

	
	
		

	
		
