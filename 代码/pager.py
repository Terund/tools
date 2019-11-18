class Pager:
    def __init__(self, data, page_size):
        self.data = data  # 总数据
        self.page_size = page_size  # 单页大小
        self.is_start = False
        self.is_end = False
        self.data_count = len(data)
        self.next_page = 0  # 下一页
        self.previous_page = 0  # 上一页
        self.page_num = self.data_count / page_size  # 总页数
        if self.page_num == int(self.page_num):
            self.page_num = int(self.page_num)
        else:
            self.page_num = int(self.page_num) + 1

    def page(self, page):
        """
        获取一页的数据
        :param page: 要返回数据的页码
        :return: 如果页码超过总页码，返回空，否则返回一页的数据
        """
        if page > self.page_num:
            return []
        self.next_page = page + 1
        self.previous_page = page - 1
        if page == 1:
            self.is_start = True
        elif page == self.page_num:
            self.is_end = True
        if self.is_end:
            return self.data[(page - 1) * self.page_size:]
        else:
            return self.data[(page - 1) * self.page_size:page * self.page_size]
