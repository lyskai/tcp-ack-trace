from bokeh.plotting import figure, output_notebook, show

hdd_hard_start_xmit_ack_list = []
dp_tx_send_msdu_single_ack_list = []


def draw():
    plot = figure(title="ack", x_axis_label='x', y_axis_label='y')

    idx = 0
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for item in hdd_hard_start_xmit_ack_list:
        x1.append(idx)
        y1.append(item)
        idx += 1
    plot.line(x1, y1, legend="hdd_hard_start_xmit", line_color = "blue", line_width=2)

    idx = 0
    for item in dp_tx_send_msdu_single_ack_list:
        x2.append(idx+1000)
        y2.append(item)
        idx += 1
    plot.line(x2, y2, legend="dp_tx_send_msdu_single_ack_list", line_color = "red", line_width=2)

    show(plot)

def parse_ack(file):
    file_handle = open(file, 'r')
    line = file_handle.readline()
    while line:
        ack = line.find("ack 1")
        if ack !=-1 :
            hdd_hard_start_xmit = line.find("hdd_hard_start_xmit")
            if hdd_hard_start_xmit != -1:
                hdd_hard_start_xmit_ack_list.append(line.split()[3][:-1])
                #print(line.split()[3][:-1])
                line = file_handle.readline()
                continue
            dp_tx_send_msdu_single = line.find("dp_tx_send_msdu_single")
            if dp_tx_send_msdu_single != -1:
                dp_tx_send_msdu_single_ack_list.append(line.split()[3][:-1])
                #print(line.split()[3][:-1])
                line = file_handle.readline()
                continue
        else:
            line = file_handle.readline()
    file_handle.close()
    draw()

if __name__ == "__main__":
    parse_ack("500m-10.txt")
