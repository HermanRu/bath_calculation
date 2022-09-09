import sqlite3
import pandas as pd
import plotly.express as px


def drop_t(tbl_name):
    con = sqlite3.connect('e_chem.db')
    cur = con.cursor()
    cur.execute(f'DROP TABLE IF EXISTS {tbl_name}')
    con.commit()
    con.close()


def fig_chart():
    con = sqlite3.connect('e_chem.db')
    df = pd.read_sql('SELECT * FROM bathes', con)
    fig = px.line(data_frame=df, x=df.index, y='m_H2SO4', color='bath_name')
    fig.show()


def create_percent_t():
    con = sqlite3.connect('e_chem.db')
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bathes_percents as 
        SELECT 
            bath_name,
            run,
            sub1/sum*100.0 sub1,
            sub2/sum*100.0 sub2,
            sub3/sum*100.0 sub3,
            sub4/sum*100.0 sub4,
            sub5/sum*100.0 sub5,
            sub6/sum*100.0 sub6,
            sub7/sum*100.0 sub7,
            sub8/sum*100.0 sub8,
            sub9/sum*100.0 sub9,
            sub10/sum*100.0 sub10,
            sub11/sum*100.0 sub11,
            sub12/sum*100.0 sub12,
            sub13/sum*100.0 sub13,
            sub14/sum*100.0 sub14,
            sub15/sum*100.0 sub15,
            sub16/sum*100.0 sub16,
            sub17/sum*100.0 sub17,
            sub18/sum*100.0 sub18,
            sub19/sum*100.0 sub19,
            sub20/sum*100.0 sub20,
            sub21/sum*100.0 sub21,
            sub22/sum*100.0 sub22,
            sub23/sum*100.0 sub23,
            sub24/sum*100.0 sub24,
            sub25/sum*100.0 sub25
        FROM bathes
        """)
    con.commit()
    con.close()


class Bath:
    def __init__(self, bath_name, bath_volume, bath_temp, transfer, cascade):
        self.bath_name = bath_name
        self.bath_volume = bath_volume
        self.bath_temp = bath_temp
        self.transfer = transfer
        self.cascade = cascade
        self.run = 0
        self.sub1 = 0
        self.sub2 = 0
        self.sub3 = 0
        self.sub4 = 0
        self.sub5 = 0
        self.sub6 = 0
        self.sub7 = 0
        self.sub8 = 0
        self.sub9 = 0
        self.sub10 = 0
        self.sub11 = 0
        self.sub12 = 0
        self.sub13 = 0
        self.sub14 = 0
        self.sub15 = 0
        self.sub16 = 0
        self.sub17 = 0
        self.sub18 = 0
        self.sub19 = 0
        self.sub20 = 0
        self.sub21 = 0
        self.sub22 = 0
        self.sub23 = 0
        self.sub24 = 0
        self.sub25 = 0

        self.drain_sub1 = 0
        self.drain_sub2 = 0
        self.drain_sub3 = 0
        self.drain_sub4 = 0
        self.drain_sub5 = 0
        self.drain_sub6 = 0
        self.drain_sub7 = 0
        self.drain_sub8 = 0
        self.drain_sub9 = 0
        self.drain_sub10 = 0
        self.drain_sub11 = 0
        self.drain_sub12 = 0
        self.drain_sub13 = 0
        self.drain_sub14 = 0
        self.drain_sub15 = 0
        self.drain_sub16 = 0
        self.drain_sub17 = 0
        self.drain_sub18 = 0
        self.drain_sub19 = 0
        self.drain_sub20 = 0
        self.drain_sub21 = 0
        self.drain_sub22 = 0
        self.drain_sub23 = 0
        self.drain_sub24 = 0
        self.drain_sub25 = 0

        self.dosing_sub1 = 0
        self.dosing_sub2 = 0
        self.dosing_sub3 = 0
        self.dosing_sub4 = 0
        self.dosing_sub5 = 0
        self.dosing_sub6 = 0
        self.dosing_sub7 = 0
        self.dosing_sub8 = 0
        self.dosing_sub9 = 0
        self.dosing_sub10 = 0
        self.dosing_sub11 = 0
        self.dosing_sub12 = 0
        self.dosing_sub13 = 0
        self.dosing_sub14 = 0
        self.dosing_sub15 = 0
        self.dosing_sub16 = 0
        self.dosing_sub17 = 0
        self.dosing_sub18 = 0
        self.dosing_sub19 = 0
        self.dosing_sub20 = 0
        self.dosing_sub21 = 0
        self.dosing_sub22 = 0
        self.dosing_sub23 = 0
        self.dosing_sub24 = 0
        self.dosing_sub25 = 0

    def print_bath_par(self):
        s = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10',
             'sub11', 'sub12', 'sub13', 'sub14', 'sub15', 'sub16', 'sub17', 'sub18', 'sub19', 'sub20',
             'sub21', 'sub22', 'sub23', 'sub24', 'sub25']
        print("Bath status:", self.bath_name, self.bath_volume, self.bath_temp)
        # print(self.s[0])
        # for i in range(len(s)):
        #     print(self.sub1)
        # print("Total volume:", self.m_H2O + self.m_H2SO4)

    def add_comps(self, lst):
        """
        list with dosing
        """
        self.sub1 += lst[0]
        self.sub2 += lst[1]
        self.sub3 += lst[2]
        self.sub4 += lst[3]
        self.sub5 += lst[4]
        self.sub6 += lst[5]
        self.sub7 += lst[6]
        self.sub8 += lst[7]
        self.sub9 += lst[8]
        self.sub10 += lst[9]
        self.sub11 += lst[10]
        self.sub12 += lst[11]
        self.sub13 += lst[12]
        self.sub14 += lst[13]
        self.sub15 += lst[14]
        self.sub16 += lst[15]
        self.sub17 += lst[16]
        self.sub18 += lst[17]
        self.sub19 += lst[18]
        self.sub20 += lst[19]
        self.sub21 += lst[20]
        self.sub22 += lst[21]
        self.sub23 += lst[22]
        self.sub24 += lst[23]
        self.sub25 += lst[24]

    def add_comps_to_drain(self, lst):
        """
        list with dosing
        """
        self.drain_sub1 -= lst[0]
        self.drain_sub2 -= lst[1]
        self.drain_sub3 -= lst[2]
        self.drain_sub4 -= lst[3]
        self.drain_sub5 -= lst[4]
        self.drain_sub6 -= lst[5]
        self.drain_sub7 -= lst[6]
        self.drain_sub8 -= lst[7]
        self.drain_sub9 -= lst[8]
        self.drain_sub10 -= lst[9]
        self.drain_sub11 -= lst[10]
        self.drain_sub12 -= lst[11]
        self.drain_sub13 -= lst[12]
        self.drain_sub14 -= lst[13]
        self.drain_sub15 -= lst[14]
        self.drain_sub16 -= lst[15]
        self.drain_sub17 -= lst[16]
        self.drain_sub18 -= lst[17]
        self.drain_sub19 -= lst[18]
        self.drain_sub20 -= lst[19]
        self.drain_sub21 -= lst[20]
        self.drain_sub22 -= lst[21]
        self.drain_sub23 -= lst[22]
        self.drain_sub24 -= lst[23]
        self.drain_sub25 -= lst[24]

    def add_comps_to_dosing(self, lst):
        """
        list with dosing
        """
        self.dosing_sub1 += lst[0]
        self.dosing_sub2 += lst[1]
        self.dosing_sub3 += lst[2]
        self.dosing_sub4 += lst[3]
        self.dosing_sub5 += lst[4]
        self.dosing_sub6 += lst[5]
        self.dosing_sub7 += lst[6]
        self.dosing_sub8 += lst[7]
        self.dosing_sub9 += lst[8]
        self.dosing_sub10 += lst[9]
        self.dosing_sub11 += lst[10]
        self.dosing_sub12 += lst[11]
        self.dosing_sub13 += lst[12]
        self.dosing_sub14 += lst[13]
        self.dosing_sub15 += lst[14]
        self.dosing_sub16 += lst[15]
        self.dosing_sub17 += lst[16]
        self.dosing_sub18 += lst[17]
        self.dosing_sub19 += lst[18]
        self.dosing_sub20 += lst[19]
        self.dosing_sub21 += lst[20]
        self.dosing_sub22 += lst[21]
        self.dosing_sub23 += lst[22]
        self.dosing_sub24 += lst[23]
        self.dosing_sub25 += lst[24]

    def sum_comps(self):
        return (self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5 + self.sub6 + self.sub7 +
                self.sub8 + self.sub9 + self.sub10 + self.sub11 + self.sub12 + self.sub13 + self.sub14 +
                self.sub15 + self.sub16 + self.sub17 + self.sub18 + self.sub19 + self.sub20 + self.sub21 +
                self.sub22 + self.sub23 + self.sub24 + self.sub25)

    def set_run(self, run):
        self.run = run

    def save_param(self):
        con = sqlite3.connect('e_chem.db')
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS bathes (
            bath_name   text,
            bath_volume real,
            bath_temp   real,
            transfer    real,
            cascade     real,
            run         real,
            sub1        real,
            sub2        real,
            sub3        real,
            sub4        real,
            sub5        real,
            sub6        real,
            sub7        real,
            sub8        real,
            sub9        real,
            sub10       real,
            sub11       real,
            sub12       real,
            sub13       real,
            sub14       real,
            sub15       real,
            sub16       real,
            sub17       real,
            sub18       real,
            sub19       real,
            sub20       real,
            sub21       real,
            sub22       real,
            sub23       real,
            sub24       real,
            sub25       real,
            sum         real
        );""")

        cur.execute("INSERT INTO bathes VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",
                    (self.bath_name, self.bath_volume, self.bath_temp, self.transfer, self.cascade, self.run,
                     self.sub1, self.sub2, self.sub3, self.sub4, self.sub5, self.sub6, self.sub7,
                     self.sub8, self.sub9, self.sub10, self.sub11, self.sub12, self.sub13, self.sub14,
                     self.sub15, self.sub16, self.sub17, self.sub18, self.sub19, self.sub20, self.sub21,
                     self.sub22, self.sub23, self.sub24, self.sub25,
                     (self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5 + self.sub6 + self.sub7 +
                      self.sub8 + self.sub9 + self.sub10 + self.sub11 + self.sub12 + self.sub13 + self.sub14 +
                      self.sub15 + self.sub16 + self.sub17 + self.sub18 + self.sub19 + self.sub20 + self.sub21 +
                      self.sub22 + self.sub23 + self.sub24 + self.sub25)
                     ))
        con.commit()
        con.close()

    def save_dosing(self):
        con = sqlite3.connect('e_chem.db')
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS dosing (
            bath_name   text,
            run         real,
            sub1        real,
            sub2        real,
            sub3        real,
            sub4        real,
            sub5        real,
            sub6        real,
            sub7        real,
            sub8        real,
            sub9        real,
            sub10       real,
            sub11       real,
            sub12       real,
            sub13       real,
            sub14       real,
            sub15       real,
            sub16       real,
            sub17       real,
            sub18       real,
            sub19       real,
            sub20       real,
            sub21       real,
            sub22       real,
            sub23       real,
            sub24       real,
            sub25       real
        );""")

        cur.execute("INSERT INTO dosing VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (
            self.bath_name,
            self.run,
            self.dosing_sub1,
            self.dosing_sub2,
            self.dosing_sub3,
            self.dosing_sub4,
            self.dosing_sub5,
            self.dosing_sub6,
            self.dosing_sub7,
            self.dosing_sub8,
            self.dosing_sub9,
            self.dosing_sub10,
            self.dosing_sub11,
            self.dosing_sub12,
            self.dosing_sub13,
            self.dosing_sub14,
            self.dosing_sub15,
            self.dosing_sub16,
            self.dosing_sub17,
            self.dosing_sub18,
            self.dosing_sub19,
            self.dosing_sub20,
            self.dosing_sub21,
            self.dosing_sub22,
            self.dosing_sub23,
            self.dosing_sub24,
            self.dosing_sub25))
        con.commit()
        con.close()

    def save_drains(self):
        con = sqlite3.connect('e_chem.db')
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS drains (
            bath_name   text,
            run         real,
            sub1        real,
            sub2        real,
            sub3        real,
            sub4        real,
            sub5        real,
            sub6        real,
            sub7        real,
            sub8        real,
            sub9        real,
            sub10       real,
            sub11       real,
            sub12       real,
            sub13       real,
            sub14       real,
            sub15       real,
            sub16       real,
            sub17       real,
            sub18       real,
            sub19       real,
            sub20       real,
            sub21       real,
            sub22       real,
            sub23       real,
            sub24       real,
            sub25       real
        );""")

        cur.execute("INSERT INTO drains VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (
            self.bath_name,
            self.run,
            self.drain_sub1,
            self.drain_sub2,
            self.drain_sub3,
            self.drain_sub4,
            self.drain_sub5,
            self.drain_sub6,
            self.drain_sub7,
            self.drain_sub8,
            self.drain_sub9,
            self.drain_sub10,
            self.drain_sub11,
            self.drain_sub12,
            self.drain_sub13,
            self.drain_sub14,
            self.drain_sub15,
            self.drain_sub16,
            self.drain_sub17,
            self.drain_sub18,
            self.drain_sub19,
            self.drain_sub20,
            self.drain_sub21,
            self.drain_sub22,
            self.drain_sub23,
            self.drain_sub24,
            self.drain_sub25))
        con.commit()
        con.close()


class Substance:
    def __init__(self, sub_num, name, conc, density, mol):
        self.sub_num = sub_num
        self.name = name
        self.conc = conc
        self.density = density
        self.mol = mol

    def save_substances(self):
        con = sqlite3.connect('e_chem.db')
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS substance (
            sub_num     text,
            name        text,
            conc        real,
            density     real,
            mol         real
            );
            """)
        cur.execute("INSERT INTO substance VALUES(?,?,?,?,?);", (
            self.sub_num,
            self.name,
            self.conc,
            self.density,
            self.mol))
        con.commit()
        con.close()


def main():
    drop_t('bathes')
    drop_t('dosing')
    drop_t('drains')
    drop_t('substance')

    subs = pd.read_excel('bath_recipes.xlsx', sheet_name='Substance')
    substance_lst = subs.cl_name.to_list()
    for i in range(len(substance_lst)):
        substance_lst[i] = Substance(subs.loc[i, 'cl_name'],
                                     subs.loc[i, 'name'],
                                     subs.loc[i, 'conc'],
                                     subs.loc[i, 'density'],
                                     subs.loc[i, 'mol'])
        substance_lst[i].save_substances()
        # print(substance_lst[i].__dict__)

    bathes = pd.read_excel('bath_recipes.xlsx', sheet_name='Bathes')

    bath_lst = bathes.iloc[0, ].to_list()[1:]
    for i in range(len(bath_lst)):
        bath_lst[i] = Bath(bathes[i + 1].to_list()[1],
                           bathes[i + 1].to_list()[2],
                           bathes[i + 1].to_list()[3],
                           bathes[i + 1].to_list()[4],
                           bathes[i + 1].to_list()[5])
        # print(bath_lst[i].__dict__)

    print('Fist filling')
    recipe = pd.read_excel('bath_recipes.xlsx', sheet_name='Recipe', skiprows=1)
    for i in range(len(bath_lst)):
        bath_lst[i].add_comps(recipe[recipe.dosing == 'first_filling'][i + 1].fillna(0).to_list())
        bath_lst[i].add_comps_to_dosing(recipe[recipe.dosing == 'first_filling'][i + 1].fillna(0).to_list())
        # print(bath_lst[i].__dict__)
        # print(bath_lst[i].sum_comps())
    print('Fist filling done')

    for run in range(1, 101):
        for i in range(len(bath_lst)):
            fraction_lst = [bath_lst[i].transfer * bath_lst[i].sub1 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub2 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub3 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub4 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub5 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub6 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub7 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub8 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub9 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub10 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub11 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub12 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub13 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub14 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub15 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub16 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub17 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub18 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub19 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub20 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub21 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub22 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub23 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub24 / bath_lst[i].sum_comps(),
                            bath_lst[i].transfer * bath_lst[i].sub25 / bath_lst[i].sum_comps()]
            # унос из ванны:
            bath_lst[i].add_comps([i * (-1) for i in fraction_lst])
            # обновление:
            bath_lst[i].add_comps(recipe[recipe.dosing == 'dosing'][i + 1].fillna(0).to_list())
            bath_lst[i].add_comps_to_dosing(recipe[recipe.dosing == 'dosing'][i + 1].fillna(0).to_list())
            # перенос загрязнений в следующую ванну:
            if i < len(bath_lst) - 1:
                bath_lst[i + 1].add_comps(fraction_lst)
            # каскад:
            if bath_lst[i].cascade > 0:
                fraction_lst = [bath_lst[i].cascade * bath_lst[i].sub1 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub2 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub3 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub4 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub5 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub6 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub7 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub8 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub9 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub10 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub11 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub12 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub13 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub14 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub15 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub16 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub17 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub18 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub19 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub20 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub21 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub22 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub23 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub24 / bath_lst[i].sum_comps(),
                                bath_lst[i].cascade * bath_lst[i].sub25 / bath_lst[i].sum_comps()]
                bath_lst[i].add_comps([i * (-1) for i in fraction_lst])
                bath_lst[i - 1].add_comps(fraction_lst)

            # Проверка объема, перелив
            delta_vol = bath_lst[i].bath_volume - bath_lst[i].sum_comps()
            if delta_vol < 0:
                fraction_lst = [delta_vol * bath_lst[i].sub1 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub2 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub3 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub4 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub5 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub6 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub7 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub8 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub9 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub10 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub11 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub12 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub13 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub14 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub15 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub16 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub17 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub18 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub19 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub20 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub21 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub22 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub23 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub24 / bath_lst[i].sum_comps(),
                                delta_vol * bath_lst[i].sub25 / bath_lst[i].sum_comps()]
                bath_lst[i].add_comps(fraction_lst)
                bath_lst[i].add_comps_to_drain(fraction_lst)
            elif delta_vol > 0 and i != len(bath_lst) - 1:
                bath_lst[i].sub1 += delta_vol
                bath_lst[i].dosing_sub1 += delta_vol

                # изменение счетчика ванны и сохранение
            bath_lst[i].set_run(run)
            bath_lst[i].save_param()
            bath_lst[i].save_dosing()
            bath_lst[i].save_drains()
        print("Run", run)

    drop_t('bathes_percents')
    create_percent_t()

    # con = sqlite3.connect('e_chem.db')
    # df1 = pd.read_sql('SELECT * FROM bathes', con)
    # df2 = pd.read_sql('SELECT * FROM dosing', con)
    # df3 = pd.read_sql('SELECT * FROM drains', con)
    # df1.to_csv(r'c:\Шелопин\ElectroPlating\bath_conc.csv', index=False)
    # df2.to_csv(r'c:\Шелопин\ElectroPlating\bath_dosing.csv', index=False)
    # df3.to_csv(r'c:\Шелопин\ElectroPlating\bath_drains.csv', index=False)


if __name__ == "__main__":
    main()
