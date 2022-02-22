# this is a helpful fucntions.
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    # here we create byteBuffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    plt.title("All Products", fontdict =font1)
    plt.plot(x,y, marker = 'o')
    plt.xticks(rotation=45)
    plt.xlabel('Product Name', fontdict=font2)
    plt.ylabel('Product Price', fontdict=font2)
    plt.tight_layout()
    graph = get_graph()
    return graph

# this is used for order
def get_plot1(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title("All Order")
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Product-Quantity and Product Price')
    plt.ylabel('Product name')
    plt.tight_layout()
    graph = get_graph()
    return graph