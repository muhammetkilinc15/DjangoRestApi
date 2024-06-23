# Django Rest Api Framework

**Django Rest Api Hakkında Genel Bilgi**

Django Rest Framework (DRF), Django üzerine inşa edilmiş, güçlü ve esnek bir toolkit sağlayan bir kütüphanedir. Web API'leri oluşturmak için kullanılır. 
Genel Yapısı şu şekildedir: 

**Temel Özellikler**

* **Serializer'lar**: Veritabanı sorgularını ve Python veri yapılarını JSON gibi formatlara dönüştürmek için kullanılır. DRF'de ModelSerializer sınıfı, Django modellerini kolayca serialize edebilmenizi sağlar.

* **Views ve ViewSets**: API uç noktalarını tanımlamak için kullanılır. ViewSets, view'ları ve view logic'ini bir arada tutarak kod tekrarını azaltır.

* **Router'lar**: URL yönlendirmelerini otomatikleştirmek için kullanılır. DRF'de SimpleRouter ve DefaultRouter gibi hazır router'lar bulunur.

* **Authentication ve Authorization**: Kullanıcı doğrulaması ve yetkilendirme için kapsamlı destek sunar. Token-based, Session-based ve OAuth gibi farklı doğrulama yöntemleri entegre edilebilir.

* **Pagination, Throttling ve Filtering**: Büyük veri setleriyle çalışırken sayfalama, istek sınırlandırma ve veri filtreleme gibi özellikler sağlar.



## Kurulum

```bash
 python -m venv myenv
```
* Kurulumdan sonra activate.bat çalıştırıyoruz. 

```bash
 py myenv/scripts/activate.bat
```
* Django Kurulum
```bash
 pip install django
```

* Django Rest Api Framework Kurulum
```bash
 pip install djangorestframework
```


** Biz ekstra
```bash
 pip install django_extensions
```
# Yükleme

* Kurulum işlemleri bittikten sonra django projemizi oluşturuyoruz

```bash
 django-admin startproject newsBulten
```

* Rest Framework ve extension yüklemiştik. Onları settings.py içerisine ekliyoruz
```bash
 pip install djangorestframework


 # settings.py
INSTALLED_APPS = [
    ...

    'rest_framework',
    'django_extensions',
]
```

------------------------------------------------------------------------------
* Ana uygulamamıza alt modül eklemek için 


```bash
 py manage.py startapp news
```

ile uygulamamız genel kurum ve yükleme aşamsını bitiyoruz




