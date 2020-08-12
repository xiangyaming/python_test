# -*- coding:utf-8 -*-
# @FileName  :cb_sys_page.py
# @Time      :2020/7/16 0016 00:57
# @Author    :xiaoming
# -----------------------------------------------------


from python_web.pagelocator.cb_sys_pagelocator import cbsyspagelocator as loc
from python_web.common.basepage import BasePage



class HtDengji(BasePage):


    #切换到合同登记页面
    def ht_page(self):
        self.click_element(loc.choose_sys)
        self.click_element(loc.cb_sys)
        self.click_element(loc.ht_guanli)
        self.click_element(loc.ht_dengji)

    #新增合同
    def new_ht(self,ht_name,qsdate="2020-07-24",kgdate="2020-07-24",jgdate="2020-07-25"):
        self.click_element(loc.select_gs,"成本系统_选择公司")
        self.click_element(loc.select_cdqy_gs,"成本系统_选择项目下拉框")
        self.click_element(loc.select_proj,"成本系统_选择项目")
        self.click_element(loc.select_first_proj,"成本系统_选择第一个项目")
        self.click_element(loc.new_ht_butoon,"成本系统_新增合同按钮")
        self.switch_window("切换窗口")
        self.input_text(loc.ht_name_text,ht_name,"新增合同_输入合同名称")
        self.click_element(loc.choose_jia_unit_button,"新增合同_选择甲方单位")
        self.switch_iframe(loc.choose_jia_unit_ifame,"新增合同_切换甲方单位iframe")
        self.click_element(loc.choose_jia_unit,"新增合同_选择甲方单位")
        self.click_element(loc.jia_save_button,"新增合同_选择甲方单位确认按钮")
        self.driver.switch_to_defaul_content() #从iframe中退回默认页面
        self.click_element(loc.choose_yi_unit_button,"新增合同_选择单位按钮")
        self.switch_iframe(loc.choose_yi_unit_iframe, "新增合同_切换乙方单位iframe")
        self.click_element(loc.choose_yi_unit,"新增合同_选择乙方单位")
        self.click_element(loc.yi_save_button,"新增合同_选择乙方单位确认按钮")
        self.driver.switch_to_defaul_content()  # 从iframe中退回默认页面
        self.click_element(loc.he_type_select,"新增合同_选择合同类别下拉框")
        self.click_element(loc.choose_ht_type,"选择合同类别")
        self.click_element(loc.cb_guishu_select,"项目成本归属选择按钮")
        self.switch_iframe(loc.choose_proj_ifarme,"项目归属iframe")
        self.click_element(loc.proj_box,"点击选择项目复选框")
        self.click_element(loc.proj_save_button,"合同_选择项目保存按钮")
        self.driver.switch_to_defaul_content()  # 从iframe中退回默认页面
        self.input_text(loc.plan_qsdate,qsdate,"输入计划签约日期")
        self.click_element(loc.cg_type_select,"采购方式下拉框")
        self.click_element(loc.choose_cg_type,"选择采购方式")
        self.click_element(loc.new_fktj_button,"新增合同付款条件")
        self.click_element(loc.choose_kx_type_name_select)
        self.click_element(loc.choose_kx_type_name,"选择款项类别和款项名称")
        self.input_text(loc.ht_kgdate,kgdate,"输入合同开工日期")
        self.input_text(loc.ht_jgdate,jgdate,"输入合同竣工日期")
        self.input_text(loc.ht_bxdaYs,"输入合同保修期限")
        self.click_element(loc.ly_money_type)
        self.click_element(loc.choose_ly_money_type,"选择履约保证金方式")
        self.click_element(loc.ht_save_button,"合同保存按钮")
