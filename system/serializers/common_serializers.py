from gettext import translation
from locale import currency
from secrets import choice
from urllib import request
from ..models.common import *
from ..models.translations import *
from ..models.columns import Column
from rest_framework import serializers
from rest_framework.response import Response
from .user_serializers import RelatedUserSerilaizer
from ..models.translations import TranslationFromData
from ..models.users import get_current_user_language
from system import utils


# ************************ Button Serializer ******************************************

class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response
        
# ************************ Button Serializer ******************************************
class RelatedCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        exclude = ("created_time", "modified_time", "created_by")
        
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response
       
# ************************ Tag Serializer ******************************************             
class RelatedTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ("created_time", "modified_time", "created_by")
                     
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("__all__") 
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response    

# ************************ Language Serializer ******************************************
class RelatedLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        exclude = ("created_time", "modified_time", "created_by") 
      
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}} 
    
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response    

# ************************ Country Serializer ******************************************
class RelatedCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ("created_time", "modified_time", "created_by") 
  
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    
    # To return foreign key values in details
    def to_representation(self, instance):
        response = super().to_representation(instance)
        currency = RelatedCurrencySerializer(instance.currency).data
        if 'id' in currency:
            response['currency'] = RelatedCurrencySerializer(instance.currency).data
            
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
            
        return response

# ************************ State Serializer ******************************************
class RelatedStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        exclude = ("created_time","modified_time","created_by")
  
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        country = RelatedCountrySerializer(instance.country).data
        if 'id' in country:
            response['country'] = RelatedCountrySerializer(instance.country).data
        
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
            
        return response

#******************************* Stage Action Serializer *******************************

class RelatedStageActionSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    def get_label(self, obj):
        data = obj.action
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationStageAction.objects.filter(stage_action = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    class Meta:
        model = StageAction
        exclude = ("created_time","modified_time","created_by", "stage")

class StageActionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = StageAction
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}} 



# ************************ Stage Serializer ******************************************    
class RelatedStageSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    def get_label(self, obj):
        data = obj.stage
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationStage.objects.filter(stage = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    class Meta:
        model = Stage
        exclude = ("created_time","modified_time","created_by")

       
class StageSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    stage_actions = serializers.SerializerMethodField()
    
    def get_stage_actions(self, obj):
        request = self.context['request']
        stage_actions = StageAction.objects.filter()
        serializers = RelatedStageActionSerializer(stage_actions, many = True, context={'request': request})
        return serializers.data
    
    def get_label(self, obj):
        data = obj.stage
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationStage.objects.filter(stage = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
        
    class Meta:
        model = Stage
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}} 
        
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response
 
# ************************ Configuration Serializer ******************************************    
class RelatedConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        exclude = ("created_time","modified_time","created_by")
        
class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
                    
        return response
    

# ************************ Territories Serializer ******************************************  
class RelatedTerritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territories
        exclude = ("created_time","modified_time","created_by")
    
class TerritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territories
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response

# ********************** Fields Serilaizer ***********************************************
# class RelatedFieldSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Field
#         fields = ("__all__") 
#         exclude = ("created_time","modified_time","created_by")
        
# class FieldSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Field
#         fields = ("__all__") 
#         read_only_fields = ("created_time", "modified_time")
#         extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         app_data = RelatedAppSerializer(instance.application).data
#         if 'id' in app_data:
#             response['application'] = RelatedAppSerializer(instance.application).data
            
#         form_data = RelatedFormSerializer(instance.form).data
#         if 'id' in form_data:
#             response['form'] = RelatedFormSerializer(instance.form).data
        
#         created_by = RelatedUserSerilaizer(instance.created_by).data
#         if 'id' in created_by:
#             response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
            
#         return response

# ************************ Choice Serializer ******************************************
class RelatedChoiceSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
       
    def get_label(self, obj):
        data = obj.choice
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationChoice.objects.filter(choice = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    
    
    class Meta:
        model = Choice
        fields = ("id","choice","label")
        
class ChoiceSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    def get_label(self, obj):
        data = obj.choice
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationChoice.objects.filter(choice = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    
    class Meta:
        model = Choice
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        choice = instance.choice
        if choice:
            response['choice'] = utils.decode_api_name(choice)
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data

        request = self.context['request']
        form = RelatedFormSerializer(instance.form, context={'request': request}).data
        if 'id' in form:
            response['form'] = RelatedFormSerializer(instance.form, context={'request': request}).data
            
        return response

    def validate(self, data):
        choice = data.get('choice')
        data['choice'] = utils.encode_api_name(choice)
        return data
    
# ************************ List Serializer ****************************************** 
class RelatedListSerializer(serializers.ModelSerializer):
    columns = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    def get_label(self, obj):
        data = obj.list
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationList.objects.filter(list = obj.id, translation__language_name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    
    def get_columns(self, obj):
        request = self.context['request']
        list_id = obj.id
        list_queryset = Column.objects.filter(list = list_id).order_by('position')
        serializer = RelatedColumnsSerializer(list_queryset, many = True, context={'request': request})         
        return serializer.data
    
    class Meta:
        model = List
        exclude = ("created_time","modified_time","created_by")
    
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context['request']
        form = RelatedFormSerializer(instance.form, context={'request': request}).data
        if 'id' in form:
            data = RelatedFormSerializer(instance.form, context={'request': request}).data
            response['form'] = data['form'] if data else None
            
        return response
    
class ListSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    columns = serializers.SerializerMethodField()
    def get_label(self, obj):
        data = obj.list
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationList.objects.filter(list = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
        
    def get_columns(self, obj):
        request = self.context['request']
        list_id = obj.id
        list_queryset = Column.objects.filter(list = list_id).order_by('position')
        serializer = RelatedColumnsSerializer(list_queryset, many = True, context={'request': request})         
        return serializer.data
    
    class Meta:
        model = List
        exclude = ("created_time","modified_time","created_by")
    class Meta:
        model = List
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    
    
    def validate(self, data):
        list = data.get('list')
        data['list'] = utils.encode_api_name(list)
        return data
    
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        list = instance.list
        if list:
            response['list'] = utils.decode_api_name(list)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        
        request = self.context['request']
        form = RelatedFormSerializer(instance.form, context={'request': request}).data
        if 'id' in form:
            response['form'] = RelatedFormSerializer(instance.form, context={'request': request}).data
        
        return response


# ************************ Columns Serializer ****************************************** 
class RelatedColumnsSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    def get_label(self, obj):
        data = obj.column
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationColumn.objects.filter(column = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    class Meta:
        model = Column
        exclude = ("created_time","modified_time","created_by","list")

class ColumnsSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    def get_label(self, obj):
        data = obj.column
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationColumn.objects.filter(column = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    class Meta:
        model = Column
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context['request']
        column = instance.column  
        if column:
            response['column'] = utils.decode_api_name(column)
        list_data = RelatedListSerializer(instance.list, context={'request': request}).data        
        if 'id' in list_data:
            data = RelatedListSerializer(instance.list, context={'request': request}).data
            list = data.pop('columns')
            response['list'] = data
        return response

    def validate(self, data):
        column = data.get('column')
        data['column'] = utils.encode_api_name(column)
        return data
# ************************ Menu Serializer ******************************************
class RelatedMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        exclude = ("created_time","modified_time","created_by")
         
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        
    # To return forign key values in detail
    def to_representation(self, instance):
        response = super().to_representation(instance)
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        request = self.context['request']
        list_data = RelatedListSerializer(instance.list, context={'request': request}).data
        if 'id' in list_data:
            response['list'] = RelatedListSerializer(instance.list, context={'request': request}).data
            
        return response


# ************************ Form Serializer ******************************************  
class RelatedFormSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    def get_label(self, obj):
        data = obj.form
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationForm.objects.filter(form = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    class Meta:
        model = Form
        exclude = ("created_time","modified_time","created_by")
   
class FormSerializer(serializers.ModelSerializer):
    form_list = serializers.SerializerMethodField()
    form_data = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    def get_form_list(self,obj):
        request = self.context['request']
        form_list = FormList.objects.filter(form = obj.id).order_by('position')
        serializer = RelatedFormListSerializer(form_list, many = True, context={'request': request})  
        return serializer.data
    
    def get_form_data(self,obj):
        request = self.context['request']
        form_data = FormData.objects.filter(form = obj.id).order_by('position')
        serializer = RelatedFormDataSerializer(form_data, many = True, context={'request': request})  
        return serializer.data
    
    def get_label(self, obj):
        data = obj.form
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationForm.objects.filter(form = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    
    class Meta:
        model = Form
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        form = instance.form  
        if form:
            response['form'] = utils.decode_api_name(form)          
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response 

    def validate(self, data):
        form = data.get('form')
        data['form'] = utils.encode_api_name(form)
        return data
    
class RelatedFormListSerializer(serializers.ModelSerializer):        
    class Meta:
        model = FormList
        exclude = ("created_time", "modified_time","form","created_by")
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context['request']
        list = RelatedCurrencySerializer(instance.list).data
        if 'id' in list:
            response['list'] = RelatedListSerializer(instance.list, context={'request': request}).data
        
        return response

class FormListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormList
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context['request']
        form = RelatedFormSerializer(instance.form, context={'request': request}).data
        if 'id' in form:
            response['form'] = RelatedFormSerializer(instance.form, context={'request': request}).data
            
        list = RelatedListSerializer(instance.list, context={'request': request}).data
        if 'id' in list:
            response['list'] = RelatedListSerializer(instance.list, context={'request': request}).data
            
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response

class RelatedTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ("id","label")
    
class RelatedFormDataSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    default = serializers.SerializerMethodField()
    
    def get_choices(self, obj):
        form_id = obj.form.id
        data = obj.data
        request = self.context['request']
        
        if data == 'State' or data == 'state':
            get_state = State.objects.filter().all()
            serializers = RelatedStateSerializer(get_state,many=True)
            return_data =[{"id":value['id'], "label": value['name']}
                           for value in serializers.data]
        
        elif data == 'Country' or data == 'country':
            get_country = Country.objects.filter().all()
            serializers = RelatedCountrySerializer(get_country,many=True)
            return_data =[{"id":value['id'], "label": value['name']}
                           for value in serializers.data]
        
        elif data == 'Language' or data == 'language':
            get_language = Language.objects.filter().all()
            serializers = RelatedLanguageSerializer(get_language,many=True)
            return_data =[{"id":value['id'], "label": value['name']}
                           for value in serializers.data]
            
        elif data == 'Stage' or data == 'stage':
            get_stage = Stage.objects.filter().all()
            serializers = RelatedStageSerializer(get_stage,many=True)
            return_data =[{"id":value['id'], "label": value['stage']}
                           for value in serializers.data]
            
        elif 'currency'in data or 'Currency' in data:
            get_currency = Currency.objects.filter().all()
            serializers = RelatedCurrencySerializer(get_currency,many=True)
            return_data =[{"id":value['id'], "label": value['code']}
                           for value in serializers.data]
        
        elif 'list' in data or 'List' in data:
            get_list = List.objects.filter().all()
            serializers = RelatedListSerializer(get_list,many=True)
            return_data =[{"id":value['id'], "label": value['label']}
                           for value in serializers.data]
        
        elif 'form' in data or 'Form' in data:
            get_form = Form.objects.filter().all()
            serializers = RelatedFormSerializer(get_form,many=True)
            return_data =[{"id":value['id'], "label": value['label']}
                           for value in serializers.data]
        
        elif 'column' in data or 'Column' in data:
            get_column = Column.objects.filter().all().order_by('position')
            serializers =RelatedColumnsSerializer(get_column,many=True)
            return_data =[{"id":value['id'], "label": value['form']}
                           for value in serializers.data]
        
        else:
            choice_queryset = Choice.objects.filter(form = form_id, selector = data)
            serializers = RelatedChoiceSerializer(choice_queryset, many=True,context={'request': request})
            return_data = [{"id":value['id'], "label": value['label']}
                           for value in serializers.data]
        return return_data
    
    def get_label(self, obj):
        data = obj.data
        user = self.context['request'].user
        language = get_current_user_language(user)
        queryset = TranslationFromData.objects.filter(formdata = obj.id, translation__language__name = language).first()
        if queryset:
            translation_id = queryset.translation.id
            translation= Translation.objects.filter(id = translation_id, language = language).first()
            serializers = RelatedTranslationSerializer(translation, many=False)
            return serializers.data['label']
        else:
            data = utils.decode_api_name(data)
            return data
    
    def get_default(self,obj):
        data = obj.data
        data = utils.decode_api_name(data)
        print(data)
        queryset = Configuration.objects.filter(configuration = data).first()
        serializers = RelatedConfigurationSerializer(queryset, many = False)
        return serializers.data['default_value']
    
    class Meta:
        model = FormData
        exclude = ("created_time", "modified_time",'form', 'created_by')
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        section = RelatedFormSectionSerializer(instance.section).data
        if 'id' in section:
            response['section'] = RelatedFormSectionSerializer(instance.section).data            
        return response 

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

    def to_representation(self, instance):
        response = super().to_representation(instance)
        request = self.context['request']
        
        data = instance.data
        if data:
            response['data'] = utils.decode_api_name(data) 
        form = RelatedFormSerializer(instance.form, context={'request': request}).data
        if 'id' in form:
            response['form'] = RelatedFormSerializer(instance.form, context={'request': request}).data
                        
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response

    def validate(self, data):
        data = data.get('data')
        data['data'] = utils.encode_api_name(data)
        return data
    
# ************************ Help Serializer ****************************************** 
class RelatedHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        exclude = ("created_time","modified_time","created_by")
    
class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ("__all__")
        read_only_fields = ("created_time", "modified_time")
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        form = RelatedFormSerializer(instance.form).data
        if 'id' in form:
            response['form'] = RelatedFormSerializer(instance.form).data
        
        stage = RelatedStageSerializer(instance.stage).data
        if 'id' in stage:
            response['stage'] = RelatedStageSerializer(instance.stage).data
        
        created_by = RelatedUserSerilaizer(instance.created_by).data
        if 'id' in created_by:
            response['created_by'] = RelatedUserSerilaizer(instance.created_by).data
        return response 

 
class RelatedFormSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSection
        exclude = ("created_time","modified_time","created_by", "form")

