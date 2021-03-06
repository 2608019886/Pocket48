class RoomNotFound(Exception):
    '''
    房间不存在
    '''
    def __str__(self):
        '''
        错误信息

        :return:
        '''
        return '房间不存在'


class UnknownError(Exception):
    '''
    未知错误类型
    '''
    def __str__(self):
        '''

        :return:
        '''
        return '未知错误'


class NetError(Exception):
    '''
    网络错误
    '''
    def __str__(self):
        '''

        :return:
        '''
        return '网络错误'
