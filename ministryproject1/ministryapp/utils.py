from django.core.mail import EmailMessage
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import base64
import io
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import base64
from PIL import Image
import io


class Util:
    @staticmethod
    def send_mail(data):
        email=EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )

        email.send()
        
    
# def get_graph():
#     buffer=BytesIO()
#     plt.savefig(buffer,format='png')
#     buffer.seek(0)
#     img_png=buffer.getvalue()
#     graph=base64.b64encode(img_png)
    
#     buffer.close()
#     return graph.decode('utf-8')

# def get_plot(x,y):
#    plt.switch_backend('AGG')
#    plt.figure(figsize=(10,5))
#    plt.title('Hello user')
#    plt.plot(x,y)
#    plt.xticks(rotation=45)
#    plt.xlabel('testX')
#    plt.ylabel('testY')
#    plt.tight_layout()
#    graph=get_graph()
#    return graph

# def create_pie_chart(labels, sizes):
#     plt.switch_backend('AGG')  # Use the 'Agg' backend for non-GUI environments
#     fig, ax = plt.subplots()
#     ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0,radius=1)
#     ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#     ax.legend(loc=3)
#     # Save the plot to a BytesIO buffer or return as an object
#     plt.tight_layout()
#     return fig




# def get_pie_chart(fig):
#     buffer = BytesIO()
#     fig.savefig(buffer, format='png')
#     plt.close(fig)  # Close the figure to release memory
#     buffer.seek(0)
#     img_png = buffer.getvalue()
#     graph = base64.b64encode(img_png).decode('utf-8')
#     buffer.close()
#     return graph



# def animate_3d_data(x_data, y_data, z_data, interval=25, xlim=(-1, 1), ylim=(-1, 1), zlim=(0, 2*np.pi)):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     line, = ax.plot([], [], [], lw=2)

#     # Set limits directly on the z-axis object
#     ax.set_xlim(xlim)
#     ax.set_ylim(ylim)
#     ax.set_zlim(zlim)

#     def animate(i):
#         line.set_data(x_data[:i], y_data[:i])
#         line.set_3d_properties(z_data[:i])
#         return line,

#     ani = FuncAnimation(fig, animate, frames=len(x_data), interval=interval)

#     # Save animation frames to a list of images
#     images = []
#     for i in range(len(x_data)):
#         fig.canvas.draw()
#         image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
#         image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
#         images.append(Image.fromarray(image))

#     # Create a BytesIO object to hold the GIF data
#     gif_bytesio = io.BytesIO()

#     # Save images as GIF and write to BytesIO
#     images[0].save(gif_bytesio, save_all=True, append_images=images[1:], format='GIF', duration=interval, loop=0)

#     # Encode GIF data as base64
#     gif_bytesio.seek(0)
#     gif_base64 = base64.b64encode(gif_bytesio.getvalue()).decode('ascii')

#     return gif_base64



# def generate_animation(x_data, y_data_sine, y_data_cosine, interval=25, xlim=(-1, 1), ylim=(-1, 1), zlim=(0, 2*np.pi)):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     line_sine, = ax.plot([], [], [], lw=2, color='r', label='Sine')
#     line_cosine, = ax.plot([], [], [], lw=2, color='g', label='Cosine')

#     # Set limits directly on the z-axis object
#     ax.set_xlim(xlim)
#     ax.set_ylim(ylim)
#     ax.set_zlim(zlim)

#     def animate(i):
#         line_sine.set_data(x_data[:i], y_data_sine[:i])
#         line_cosine.set_data(x_data[:i], y_data_cosine[:i])
#         line_sine.set_3d_properties(np.sin(x_data[:i]))
#         line_cosine.set_3d_properties(np.cos(x_data[:i]))
#         return line_sine, line_cosine

#     ani = FuncAnimation(fig, animate, frames=len(x_data), interval=interval)

#     # Save animation frames to a list of images
#     images = []
#     for i in range(len(x_data)):
#         fig.canvas.draw()
#         image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
#         image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
#         images.append(Image.fromarray(image))

#     # Create a BytesIO object to hold the GIF data
#     gif_bytesio = io.BytesIO()

#     # Save images as GIF and write to BytesIO
#     images[0].save(gif_bytesio, save_all=True, append_images=images[1:], format='GIF', duration=interval, loop=0)

#     # Encode GIF data as base64
#     gif_bytesio.seek(0)
#     gif_base64 = base64.b64encode(gif_bytesio.getvalue()).decode('ascii')

#     return gif_base64




# def generate_angle_visualization(user_angle):
#     # Convert angle to radians
#     angle_radians = np.radians(float(user_angle))

#     # Generate angle visualization
#     fig, ax = plt.subplots()
#     # Plot the angle visualization as needed
#     # Remember to save the plot to a BytesIO buffer

#     # Save plot to a BytesIO buffer
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     plt.close()

#     # Return image data
#     buffer.seek(0)
#     return buffer.getvalue()