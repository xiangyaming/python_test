# -*- coding:utf-8 -*-
# @FileName  :cb_sys_pagelocator.py
# @Time      :2020/7/16 0016 00:51
# @Author    :xiaoming
# -----------------------------------------------------

from selenium.webdriver.common.by import By

class cbsyspagelocator:
    #选择系统,!!!对于鼠标悬浮上去才能定位的元素，先鼠标悬浮，在sources中，使用ctrl+\组合键暂停js在进行定位
    choose_sys=(By.XPATH,'//div[@id="mp-app-switch"]')
    #成本系统
    cb_sys=(By.XPATH,'//a[text()="成本系统"]')
    #合同管理
    ht_guanli=(By.XPATH,'//span[text()="合同管理"]')
    #合同登记
    ht_dengji=(By.XPATH,'//a[text()="合同登记"]')
    #选择公司下拉框
    select_gs=(By.XPATH,'(//i[@class="mp-icon-arrow"])[1]')
    #选择成都区域公司
    select_cdqy_gs=(By.XPATH,'//span[text()="成都区域"]')
    #选择项目下拉框
    select_proj=(By.XPATH,'(//i[@class="mp-icon-arrow"])[2]')
    #选择第一个项目
    select_first_proj=(By.XPATH,'(//span[@class="fe-tree-node__folder-icon is-expanded"])[2]')
    #新增合同
    new_ht_butoon=(By.XPATH,'//li[@id="x_appGrid_ViewListHeader_global_toolbar-button_mAddNotContract"]')
    #合同名称输入框
    ht_name_text=(By.XPATH,'//div[@id="appForm_Sub_ContractName"]//input[@class="el-input__inner"]')
    #选择甲方单位‘+’
    choose_jia_unit_button=(By.XPATH,'//td[@data-label="甲方单位"]//i[@class="mp-icon-plus-21"]')
    # 选择甲方iframe
    choose_jia_unit_ifame = (By.XPATH, '//iframe[@id="iframe_popup_openWin_1"]')
    #选择甲方单位
    choose_jia_unit=(By.XPATH,'//td[@id="20$cell$10"]')
    #选择甲方确认按钮
    jia_save_button=(By.XPATH,'//li[@id="x_AppGrid_Toolbar_Bottom-button_mDefine"]')
    # 选择乙方单位‘+’
    choose_yi_unit_button = (By.XPATH, '//td[@data-label="乙方单位"]//i[@class="mp-icon-plus-21"]')
    # 选择乙方iframe
    choose_yi_unit_iframe = (By.XPATH, '//iframe[@id="iframe_popup_openWin_2"]')
    # 选择乙方单位
    choose_yi_unit = (By.XPATH, '//td[@id="20$cell$10"]')
    #选择一方单位确定按钮
    yi_save_button=(By.XPATH,'//div[@data-name="save"]')
    #合同类别的‘+’
    he_type_select=(By.XPATH,'//div[@id="appForm_Sub_HtTypeGUID"]//span[@class="mp-icon-arrow"]')
    #选择合同类别
    choose_ht_type=(By.XPATH,'//div[@id="mini-22$row0$undefined"]')
    #成本归属‘+’
    cb_guishu_select=(By.XPATH,'//div[@id="appForm_Sub_ProjectCostOwnerGUIDs"]//i[@class="mp-icon-plus-21"]')
    #选择项目iframe
    choose_proj_ifarme=(By.XPATH,'//iframe[@id="iframe_popup_openWin_2"]')
    #项目复选框
    proj_box=(By.XPATH,'//span[@id="mini-8$checkbox$2"]')
    #选择项目确定按钮
    proj_save_button=(By.XPATH,'//div[@data-name="save"]')
    #计划签约日期
    plan_qsdate=(By.XPATH,'//div[@id="appForm_Sub_SignDate"]//input')
    #采购方式
    cg_type_select=(By.XPATH,'//div[@id="appForm_Sub_CgMethod"]//input')
    #选择采购方式
    choose_cg_type=(By.XPATH,'//li[@id="mini-35$0"]')
    #新增付款条件按钮
    new_fktj_button=(By.XPATH,'//li[@id="appForm_Sub_subGrid_cb_HTFKCondition_ContractGUID_Grid_ViewListHeader_global_toolbar-mAdd"]')
    #款项类别及名称
    kx_type_name=(By.XPATH,'//div[@id="mini-68$90$68$editor"]//span[text()="请选择"]')
    #选择款项类别及名称下拉选项
    choose_kx_type_name_select=(By.XPATH,'//div[@id="mini-148$row0$undefined"]//span[@class="hc-tree-node__fold"]')
    # 选择款项类别及名称
    choose_kx_type_name=(By.XPATH,'//div[@id="mini-148$row1$undefined"]')
    #合同开工日期
    ht_kgdate=(By.XPATH,'//div[@id="appForm_Sub_BeginDate"]//input')
    #合同竣工日期
    ht_jgdate=(By.XPATH,'//div[@id="appForm_Sub_EndDate"]//input')
    #合同保修期限
    ht_bxdaYs=(By.XPATH,'//div[@id="appForm_Sub_BxLimit"]//input')
    #履约保证金方式
    ly_money_type=(By.XPATH,'//div[@id="appForm_Sub_x_lybzjfs"]//input')
    #选择履约保证金方式
    choose_ly_money_type=(By.XPATH,'ly_money_type=(By.XPATH,')
    #合同保存那妞
    ht_save_button=(By.XPATH,'//li[@id="appForm_Toolbar-mSave"]')

    
