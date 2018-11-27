import tempfile
import requests
import os
from django.conf import settings
from django.core import files
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import transaction

from authentication.models import User
from project.models import ProjectImage, License, Project
from tag.models import TaggedItem

users = """
ID,username,first_name,last_name,email,picture,brief_introduction,gender,interests,skills,profession,facebook_profile,intagram_profile,twitter_profile,linkedin_profile,youtube_profile
1,wmorales,William,Morales,williammorales@jointest.com,shutterstock_1180324234.jpg,¡Hola! Soy Técnico en Diseño Gráfico y Publicitario. Tengo grandes habilidades para el manejo de las fuentes tipográficas.. y la utilización de colores. Me gusta inventar tipográfias con diversas formas geométricas.,Masculino,Tipografía;Diseño Editorial;Ilustración,Adobe Illustrator; Adobe Photoshop; Adobe Indesign,Diseñador Gráfico,william.morales23,William-Morales,williamorales,williamorales,
2,sperez,Soledad,Perez,s.perez@jointest.com,shutterstock_716886988.jpg,¡Hola!  Tengo grandes habilidades para crear patrones que puedan ser utilizados para crear grandes marcas de ropa.,Femenino,Patrones;Texturas;Tejidos,Solidwork;PatternMaker,Diseñadora de Indumentaria,s.perez23,Sole Perez,y,sperez,
3,spaellada,Santiago,Paellada,s.paellada@jointest.com,shutterstock_1178622859.jpg,¡Buenas Creativos! Quiero ser parte de grandes proyectos. Hace poco me recibí y tengo muchas ganas de compartir mis conocimientos y adquirir nuevas experiencias. Gracias a todos!,Masculino,Videos para Eventos; Fotografía para Redes Sociales,Adobe Audition;Lightroom Classic,Fotografo,s.paellada23,Santi.Paellada,spaelladaa,spaelladaa,
4,jpachenega,Javier,Pachenega,solomun.pachenega@dogs.com,shutterstock_262734242.jpg,¡Hola a todos! Me encanta las técnicas y aplicaciones de la madera en los diferentes espacios externos. Trato de innovar cada día en los productos que realizo.,Masculino,Fotografía para redes sociales y eventos,Adobe Audition;Lightroom Classic; Media Encoder,Fotografo,s.pachenega,Pachenega.Javier,,,
5,sflores,Soledad,Flores,	soledadflores@jointest.com,shutterstock_209647441.jpg,¡Gente Querida! Tengo muchas ganas de compartir mis habilidades y unirme a grandes proyectos. Cuenten conmigo! Gracias a todos por aceptarme en esta gran comunidad de diseñadores.,Femenino,Fotografía para redes sociales y eventos,Adobe Audition;Lightroom Classic; Media Encoder,Fotógrafa,s.flores23,,s.flores23,s.flores23,s.flores23
6,rperez,Ruben,Perez,rubenperez@jointest.com	,shutterstock_1164370612.jpg,¡Hola! Soy especialista en patrones de confección.. con sus respectivas transformaciones o al diseño de estampados textiles. Quiero participar de los proyectos que propongan!,Masculino,Molderia;Desfiles;Telas; Texturas,Solidwork;PatternMaker,Diseñador de Indumentaria,r.perez,Ruben Perez,,r.perez,
7,rcarlo,Roberto,Carlo,rcarlo@join.test.com,shutterstock_1153500805.jpg,Creativos!! Soy un apacionado por la construcció de packaging. Creo que el envoltorio de cualquier producto es de suma importancia para la venta.,Masculino,Acuarelas;Packaging; Ilustración,Adobe Illustrator; Adobe Photoshop; Adobe Indesign;Adobe Audition. 3Dmax,Diseñador Gráfico,r.carlo,Robert Carlo,,,
8,pgilleto,Paula,Gilleto,	pgilleto@jointest.com,shutterstock_151159397.jpg,¡Hola Diseñadores! Me interesa ser parte de los proyectos que surjan para poder aportar mis ideas alocadas a lo que ustedes propongan. Me gusta ser parte de creaciones para videos. Espero poder sumarme pronto a algún proyecto,Femenino,Storyboard; Tipografía; Creatividad;Ideas innovadoras; Afiches y Folletos,Adobe Illustrator; Adobe Photoshop; Adobe Indesign;Adobe Audition. 3Dmax,Diseñadora Gráfica,pau.gilleto2,Pau Gilleto,,pau.gilleto2,pau.gilleto2
9,msolis,Mauro,Solis,m.solis@jointest.com,shutterstock_788313199.jpg,Holaaaa! Los diseñadores somos el cambio del mundo. Soy especialista en la aplicacion de estilos de pisos para las habitaciones. Me gusta estar en ésta página con mis colegas.,Masculino,Alfombras;Ceramica y Porcelanato,Solidwork;PatternMaker; Corel; Adobe Illustrator;Photoshop,Diseñador de Interiores,mau.solis,MauroSolis,mau.solis,,
10,mramirez,Matías,Ramirez,matiasramirez@jointest.com,shutterstock_771946243.jpg,¡Diseñadores! Soy un amante de los diseños de calzados. Espero poder formar parte de un gran equipo y compartir mi experiencia con ustedes.,Masculino,Calzado; Tejidos; Mayas; Patrones; Moldelería,Solidwork;PatternMaker; Corel,Diseñador de Indumentaria,mramirezss,Matías.Ramirez,m.ramirez,,m.ramirez
11,mcreche,Marcos,Creche,marcoscreche@jointest.com,shutterstock_767470705.jpg,¡Hola Chicos! El diseño es lo mas lindo que existe porque esta en todos lados. Me gusta combinar la tipografía en mis diferentes creaciones de diseño de libros y revista. Cualquier duda estoy para ayudar y servir!,Masculino,Tipografía;Diseño Editorial;Ilustración;Creatividad;Packaging,Adobe Illustrator; Adobe Photoshop; Adobe Indesign;Corel,Diseñador Gráfico,mcreche,Marcos.Creche,,,mcreche
12,mboero,María Luz,Boero,maru.boero@gmail.com,shutterstock_666258808.jpg,¡Hola a todos! Me apasiona el diseño en todos sus sentidos.. soy especialista en el uso de los programas de diseño y quiero compartir con ustedes mis habilidades y cualidades.,Femenino,Tipografía;Diseño Editorial;Ilustración;Creatividad;Packaging; Edición de Fotos,Adobe Illustrator; Adobe Photoshop; Adobe Indesign;Corel,Diseñadora Gráfica,mboeroo,Maru.Boero,,,mlboero
13,jhernández,Joaquín,Hernández,j.hernandez@jointest.com,shutterstock_611518823.jpg,¡Hola Creativos! Soy especialista en equipamiento y diseño de interiores. Me interesa aprender y formar grandes grupos de trabajos colaborativos.,Masculino,Equipamiento; Paredes; Muebles; Madera; Empapelados; Ilustración,Solidwork;PatternMaker; Corel; Adobe Illustrator; Photoshop,Diseñador de Interiores,hernandezj,,hernandezj,hernandezj,
14,jcarballo,Julian,Carballo,j.carballo@jointest.comc,shutterstock_526589545.jpg,Diseñadores.. hace poco recibí mi título en Lic. en Diseño. Me encanta la ilustración y estoy constantemente aprendiendo diferentes técnicas de dibujo para poder ser mejor cada día.,Masculino,Tipografía;Diseño Editorial;Ilustración;Creatividad;Packaging; Edición de Fotos; Páginas web,Adobe Illustrator; Adobe Photoshop; Adobe Indesign;Corel; Adobe InCopy,Diseñador Gráfico,jcarballo23,,jcarballo23,jcarballo23,jcarballo23
15,iprados,Inés,Prados,i.prados@jointest.comi,shutterstock_1006258609.jpg,¡Hola chicos! Soy diseñadora de interiores y mi desafío es unirme a grandes grupos para poder compartir mis conocimientos con otros profesionales. Podemos formar grandes equipos.,Femenino,Equipamiento; Paredes; Muebles; Madera; Empapelados; Ilustración,Adobe Ilustrator; Adobe Photoshop; Solidwork; PatternMaker; Corel,Diseñadora de Interiores,iprados23,Ines.Prados,,iprados23,
16,g.vazquez,Guillermina,Vazquez,guillermina.vazquez@jointest.com,shutterstock_733240954.jpg,Buenas! Mi desafio es plantear nuevos moldes y combinar con diseños de patrones para lograr combinar distintas disciplinas.,Femenino,Molderia;Desfiles;Telas; Texturas,Solidwork;PatternMaker,Diseñadora de Indumentaria,guillevazquez,,,,
17,fmc0208	,Federico Marcelo,Castro,fmc0208@gmail.com,shutterstock_520889956.jpg,¡Hola a todos! Me gusta compartir mis fotografías con los demás y tabajar en proyectos de gran embergadura. Espero poder sumarme a sus ideas y colaborar con grandes imágenes.,Masculino,Fotografía para redes sociales y eventos,Adobe Audition;Lightroom Classic; Media Encoder; Media Encoder,Fotógrafo,fedecastro,Fede.Castro,,fedecastro,fedecastro
18,fbernuy,Florencia,Bernuy,f.bernuy@jointest.com,shutterstock_1180837438.jpg,El diseño ediotrial es una gran herramienta hoy en día.. la cual puede ser combinada con el diseño digital. A través de la puesta en común de diferentes ideas me gustaria dar una mano en distintos proyectos. Gracias! ,Femenino,Tipografía;Diseño Editorial;Ilustración;Creatividad;Packaging; Diseño de Patrones,Adobe Illustrator; Adobe Photoshop; Adobe InDesign; Corel,Diseñadora Gráfica,fbernuy23,Florencia.Bernuy,,,fbernuy23
19,dfontanarosa,David,Fontanarosa,d.fontanarosa@jointest.com,shutterstock_394461484.jpg,¡Diseñadores! Amo la indumentaria en todo sentido y estoy dispuesto a brindar las mejores ideas. En equipo los proyectos son mejores!,Masculino,Molderia;Desfiles;Telas; Tejidos Especiales; Texturas,Solidwork;PatternMaker; Adobe Photoshop; Adobe Ilustrator,Diseñador de Indumentaria,davidfontanarosa,,,,davidfontanarosa
20,cmoyano,Celeste,Moyano,c.moyano@jointest.com,shutterstock_322118177.jpg,¡Holaaaa! Que lindo saber que hay gente de mi misma rama.. profesionales.. que quieren aprender y aportar sus técnicas. Soy una apasionada por la moda y las texturas que las telas inspiran. Espero poder colaborar en muchos proyectos. Gracias!,Femenino,Molderia;Desfiles;Telas; Texturas; Tejidos Especiales,Solidwork;PatternMaker; Adobe Photoshop; Adobe Ilustrator,Diseñadora de Indumentaria,cmoyano233,Cele.Moyano,cmoyano233,cmoyano233,
21,cguzman,Carla,Guzmán,carla.guzman@jointest.com,shutterstock_696230005.jpg,¡Woow! Los videos y fotos hoy en día son todo. En este mundo digital que se actualiza a todo momento. Es importante saber como colocar los productos para poder generar escenas increíbles.,Femenino,Videos y Fotografia para eventos y Redes Sociales,Adobe Audition;Lightroom Classic; Media Encoder,Fotografa,cguzman233,,cguzman233,,
22,bmorales	,Cecilia Belén,Morales,	ceciliabelen2595@gmail.com,shutterstock_662171107.jpg,¡Hola a todos! Soy una apasionada por las ideas alocadas y me gusta innovar en los diseño de ilustración.. editorial y tipografía. Quiero aprender y aportar mis ideas y conocimientos a los proyectos en los que pueda unirme. Gracias a todos!,Femenino,Tipografía;Diseño Editorial;Ilustración;Creatividad;Packaging; Diseño de Patrones,Adobe Illustrator; Adobe Photoshop; Adobe Indesign;Corel; 3D,Diseñadora Gráfica,ceci.morales33,Meric_ceci,ceci.morales33,ceci.morales33,ceci.morales33
23,fmartins,Franca,Martins,f.martins@jointest.comc,Franca-martins.jpg,¡Chicos.. hola a todos! Hoy el diseño nos inspira a hacer grandes cosas. Quiero aportar desde mi profesión como diseñadora de interiores. ,Femenino,Equipamiento; Paredes; Muebles; Madera; Empapelados; Ilustración,Solidwork;PatternMaker; Corel; Adobe Illustrator; Photoshop,Diseñadora de Interiores,francamartins,Fran.Martins,francamartins,,
"""

PROJECTS = """
Titulo,Descripción Corta,Descripción Larga,Licencia,Dueño,Colaboradores,Visibilidad,Estado,Tags,Imagen Principal (500x700) (LINK)
Bakery,Diseño Packaging,Handmade; calidad y frescura son las principales características de los productos que ofrece Bakery; y sobre las cuales se definió la  identidad y el diseño del packaging. Es un diseño simple; a dos tintas; donde predominan ilustraciones relacionadas al rubro de la marca; sobre un papel natural; rústico y cálido.,Licencia abierta,Carla Guzmán,María Linares - Nicol Maydana - Martina Biré,Privado,Finalizado,Packaging - Embalaje - Identidad - Sustentable,shutterstock_1038992026.jpg
Geometría natural,Decoración sustentable,Cuadros verdes que dan vida y acomapañan la estructura de los espacios; creados con madera reciclada; pinturas naturales; y plantas tanto para exterior como interior.,Licencia abierta,Mauro Solis - Paula Gilleto,Santiago Paellada - David Fontanarosa,Publico,Iniciado,Diseño de Interiores - Decoración - Verde - Jardín - Sustentable,shutterstock_471391643.jpg
Lines,Moda/Fotografía,Queremos dar un giro a la moda 2019; queremos llevar la moda line (estilo de líneas) a tu armario. Algo sofisticado; destinado a mujeres con un estilo minimalista y simple ¿Te sumas? ,Licencia cerrada,Guillermina Vazquez,Noelia Jaca- Rafael Hernádez,Publico,Finalizado,Diseño de indumentaria-Fotografía- Belleza- Lineas- Juvenil- 2019- Placard- Femenini- Minimalista,shutterstock_266547770.jpg
Tipografía Warm,Diseño tipográfico,Un proyecto destinado a generar una nueva tendencia tipográfica para ser utilizada en ambientes festivos; donde el contraste con la luz es lo que predomina. La curva y el espacio entre líneas permiten enfocar la atención de quienes miren un cartel por las calles cordobesas.,Licencia abierta,William Morales- Ruben Perez,Rafael Bernuy- Florencia Monetto,Privado,Finalizado,Colores- tipografía- letras- curvas- carteles- luces- palabras,shutterstock_1084997549.jpg
Enfoques paisajisticos,Fotografía,Si te apasiona el aire libre y tomar fotos; esté proyecto es para vos. La idea es tomar fotogrfías de los distintos lugares de las sierras de Córdoba para realizar un book de foto. ,Licencia cerrada,Soledad Flores,Cecilia Elena- Micael Sanchez- Pía Lopez,Publico,Abierto,Camara de fotos- paisajes- luz- enfoques- pregnancia,shutterstock_558890911.jpg
Ilustración tropical,Ilustración- Diseño editorial,La pluma; la tableta y el color son nuestras pasiones por la ilustración. Un trabajo ilustrativo donde se intenta dar a conocer la ilustración y la utilización de los diferentes elementos que pueden intervenir a la hora de pensar un dibujo. Respetar la gama de colores y a línea permite la unidad del diseño. En busqueda de dibujos con un estilo fresco y tropical que permitan ser leidos por si mismo.,Licencia abierta,Marcos Creche,Joel Gomez- Micaela Simes- Noel Boero- Julian Carballo,Privado,Iniciado,Punto- línea- dibujo- ilustración- papel- computadora- pincel- tableta,shutterstock_589045499-01.jpg
Loarem mercados,Identidad corporativa- Diseño gráfico,La identidad de marca permite la identificación por parte del usuario; sea donde sea que se visualize. La combinación de elementos y creación de merchandasing colaboran en la huella de la marca. Un trabajo que inivita a la innovación e inspiración para dejar una huella por los supermercados cordobeses.,Licencia cerrada,Matías Ramirez,Magalí Courel- Sol Prados,Publico,Iniciado,Merchandasing- tipografía- diseño de identidad- marca- proyecto- ,shutterstock_1130146703.png
Trajes de baño pop,Diseño de indumentaria- Diseño de identidad,Con la llegada del verano los trajes de baño son el boom del momento. Un emprendimiento que apunta a la alta costura de mayas y bikinis de colores; inspirados en la tendencia pop.¿Contamos con vos?,Licencia abierta,Celeste Moyano,Joaquin Hernández- Candelaria Molina,Privado,Abierto,Telas- mayas- colores- corte y confección-diseño de indumentaria,shutterstock_132434312.jpg
"""


def update_project_image(project, image_name):
    image_path = os.path.join(settings.BASE_DIR, static('projects/{}'.format(image_name))[1:])
    with open(image_path, 'rb') as project_image_file:
        file_name = '{}_project_picture.jpg'.format(project.id)
        project_image = ProjectImage(project=project)
        project_image.file.save(file_name, files.File(project_image_file))
        project_image.save()


def update_user_image(user, image_name):
    # Steam the image from the url
    # Save the temporary image to the model#
    # This saves the model so be sure that is it valid
    image_path = os.path.join(settings.BASE_DIR, static('users/{}'.format(image_name))[1:])
    with open(image_path, 'rb') as user_image_file:
        file_name = '{}_profile_picture.jpg'.format(user.id)
        user.picture.save(file_name, files.File(user_image_file))


def update_user_image_from_url(user, image_url):
    # Steam the image from the url
    request = requests.get(image_url, stream=True)

    url = 'https://drive.google.com/uc?id={}'

    file_id = image_url.split('/')[-2]
    image_url = url.format(file_id)

    # Was the request OK?
    if request.status_code != requests.codes.ok:
        # Nope, error handling, skip file etc etc etc
        return

    # Create a temporary file
    lf = tempfile.NamedTemporaryFile()

    # Get the filename from the url, used for saving later
    file_name = '{}_profile_picture.jpg'.format(user.username)

    # Read the streamed image in sections
    for block in request.iter_content(1024 * 8):

        # If no more file then stop
        if not block:
            break

        # Write image block to temporary file
        lf.write(block)

    # Create the model you want to save the image to

    # Save the temporary image to the model#
    # This saves the model so be sure that is it valid
    user.picture.save(file_name, files.File(lf))


def get_user_from_full_name(full_name):
    full_name = [u for u in full_name.split('-')][0].strip() if '-' in full_name else full_name
    first_name, last_name = full_name.split()
    try:
        user = User.objects.get(first_name=first_name, last_name=last_name)
    except User.DoesNotExist as e:
        user = None
    return user


def create_super_user():
    u = User(username='admin', email='fmc0208@gmail.com',
             first_name='Federico', last_name='Castro',
             is_staff=True, is_superuser=True)
    u.set_password('admin1234')
    u.save()


def load_projects():
    from project.models import Project

    Project.objects.all().delete()

    for title, short_description, long_description, lic, owner,\
        collaborators, visibility, status, tags, main_image in [e.split(',') for e in PROJECTS.split('\n') if e][1:]:
        owner = get_user_from_full_name(full_name=owner) or User.objects.get(username='admin')
        long_description = long_description.replace(';', ',')
        collaborators = [c.strip() for c in collaborators.split('-')]
        collaborators = [get_user_from_full_name(u) for u in collaborators]
        tags = [t.strip() for t in tags.split('-')]

        lic, created = License.objects.get_or_create(title=lic)

        project = Project.objects.create(
            title=title,
            brief_description=short_description,
            description=long_description,
            license=lic,
            owner=owner,
        )

        update_project_image(project, image_name=main_image)

        for tag in tags:
            ti = TaggedItem.objects.create(tag=tag.capitalize(), content_object=project)

        for c in collaborators:
            if c:
                project.collaborators.add(c)


def load_users():
    from authentication.models import User, Skill, Profession
    from project.models import Interest

    for idu, username, first_name, last_name, email, image_file_name, \
        description, gender, interests, skills, profession, \
        fbp, isp, twp, lip, ytp in [e.split(',') for e in users.split('\n') if e][1:]:

        idu = int(idu)+10
        description = description.replace('..', ',')
        skills = skills.split(';')
        interests = interests.split(';')

        user_profession, created = Profession.objects.get_or_create(title=profession.strip())

        user_skills = []
        for skill in skills:
            skill_obj, created = Skill.objects.get_or_create(title=skill.strip())
            user_skills.append(skill_obj)

        user_interests = []
        for interest in interests:
            interest_obj, created = Interest.objects.get_or_create(title=interest.strip())
            user_interests.append(interest_obj)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        else:
            user.delete()
        finally:
            user = User.objects.create(
                username=username, brief_introduction=description,
                first_name=first_name, last_name=last_name,
                email=email, profession=user_profession,
                city='Córdoba',
                country='Argentina',
                postal_code='5000',
                address_line_1='Avenida Ejemplo 123',
                address_line_2='Córdoba capital',
                facebook_profile=fbp,
                twitter_profile=twp,
                youtube_profile=ytp,
                linkedin_profile=lip,
                instagram_profile=isp
            )
            user.skills.set(user_skills)
            user.profession = user_profession
            user.interests.set(user_interests)
            update_user_image(user, image_file_name)
            user.save()


def load_initial_data():
    with transaction.atomic():
        User.objects.all().delete()
        Project.objects.all().delete()
        create_super_user()
        load_users()
        load_projects()

