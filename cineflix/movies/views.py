from django.shortcuts import render,redirect

from django.views import View

from . models import Movie,IndustryChoices,GenreChoices,ArtistsChoices,LanguagesChoices,CerificationChoices

from .forms import MovieForm

# Create your views here.

class HomeView(View):

    template = 'home.html'

    def get(self,request,*args,**kwargs):

        data = {'page':'Home'}

        return render(request,self.template,context=data)
    
class MovieView(View):

    template = 'movies/movie-list.html'

    def get(self,request,*args,**kwargs):

        movies = Movie.objects.all()

        data = {'page':'Movies','movies':movies}

        return render(request,self.template,context=data) 
    
    # normal way
    
# class MovieCreateView(View):

#     def get(self,request,*args,**kwargs):

#         industry_choices = IndustryChoices

#         genre_choices = GenreChoices

#         languages_choices = LanguagesChoices

#         artists_choices = ArtistsChoices

#         certification_choices = CerificationChoices

#         data = {
#                 'page':'Create Movie',
#                 'industry_choices':industry_choices,
#                 'genre_choices':genre_choices,
#                 'languages_choices':languages_choices,
#                 'artists_choices':artists_choices,
#                 'certification_choices': certification_choices
#                 }

#         return render(request,'movies/movie-create.html',context=data)
    
#     def post(self,request,*args,**kwargs):

#         movie_data = request.POST

#         name = movie_data.get('name')

#         photo = request.FILES.get('photo')

#         description = movie_data.get('description')

#         release_date = movie_data.get('release_date')

#         runtime = movie_data.get('runtime')

#         certification = movie_data.get('certification')

#         industry = movie_data.get('industry')

#         languages = movie_data.get('languages')

#         genre = movie_data.get('genre')

#         artists = movie_data.get('artists')

#         video = movie_data.get('video')

#         tags = movie_data.get('tags')

#         Movie.objects.create(name=name,
#                              photo=photo,
#                              description=description,
#                              release_date=release_date,
#                              industry=industry,
#                              runtime=runtime,
#                              certification=certification,
#                              genre=genre,
#                              artists=artists,
#                              video=video,
#                              tags=tags,
#                              languages=languages)

#         return redirect('movie-list')
    
class MovieCreateView(View):

    form_class = MovieForm

    template = 'movies/movie-create.html'

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'page':'Create Movie',
                'form':form
                }

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():

            form.save()
            
            return redirect('movie-list')
        
        data = {'form':form,'page':'Create Movie'}
        
        return  render(request,self.template,context=data)
    
#  ---implementing with id--- 

# class MovieDetailsView(View):

#     template = 'movies/movie-details.html'

#     def get(self,request,*args,**kwargs):

#         id = kwargs.get('id')

#         movie = Movie.objects.get(id=id)

#         data = {'movie':movie,'page':movie.name}
        
#         return render(request,self.template,context=data)
    
class MovieDetailsView(View):

    template = 'movies/movie-details.html'

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        data = {'movie':movie,'page':movie.name}
        
        return render(request,self.template,context=data)

