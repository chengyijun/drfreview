from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from api.models import Classes, Student


# Create your views here.


class StudentSeri(ModelSerializer):
    classesx = serializers.HyperlinkedIdentityField(view_name="api:test3",
                                                    lookup_field="classes_id",
                                                    lookup_url_kwarg="id")

    # source 表示数据的来源  来源于 classes模型的 classes_name字段
    # classes_name = serializers.CharField(source='classes.classes_name')

    class Meta:
        model = Student
        fields = "__all__"
        # 默认depth=0 数字越大 通过外键跨的表越多
        # depth = 1


class ClassesSeri(ModelSerializer):
    # 必须与模型外键 反向查找别名一致才行 related_name='stus'
    stus = StudentSeri(many=True)

    # studs = serializers.SerializerMethodField()
    # cn = serializers.CharField(source="classes_name")

    class Meta:
        model = Classes
        fields = "__all__"

    def get_stus(self, obj: Classes):
        print("*******", obj)
        print("^^^^^^^^^^", obj.stus.values("id", "stu_name"))
        return obj.stus.values("id", "stu_name")

    def create(self, validated_data):
        # 重写save() 让其支持级联保存
        print("55555", validated_data)
        stus = validated_data.pop("stus")
        print(stus)
        class_obj = Classes.objects.create(**validated_data)

        stu_objs = [
            Student.objects.create(**stu, classes_id=class_obj.id)
            for stu in stus
        ]
        print("xxxxxxx", stu_objs)
        class_obj.stus.set = stu_objs
        return class_obj


class TestView(APIView):

    # authentication_classes = [MyAuth]

    def get(self, request: Request, *args, **kwargs):
        # cl = Classes()
        # cl.classes_name = "319班"
        # cl.save()
        # student = Student()
        # student.stu_name = "子龙"
        # student.classes = cl
        # student.save()
        # print("创建成功")
        # Student.objects.create(stu_name="abel",
        #                        classes=Classes(classes_name="309班"))

        cl = Classes.objects.first()
        # print("----------", cl.student_set.all())
        # print("----------", cl.stus.all())
        data = ClassesSeri(instance=cl).data
        print(data)

        return Response(data=data)


class Test2View(APIView):

    def get(self, request: Request, *args, **kwargs):
        """级联保存数据

        Args:
            request (Request): _description_

        Returns:
            _type_: _description_
        """
        data = {
            "classes_name": "jk班22",
            "stus": [{
                "stu_name": "云长22",
            }, {
                "stu_name": "孟德22",
            }]
        }

        cs = ClassesSeri(data=data)
        if cs.is_valid():
            print("77777777777777", cs.validated_data)
            cs.save()
        else:
            print(cs.errors)
            return Response({"code": 0})

        return Response({"code": 1})


class Test3View(APIView):

    def get(self, request: Request, *args, **kwargs):
        id = kwargs.get("id")
        stus = Classes.objects.filter(id=id).get()
        ser = ClassesSeri(instance=stus,
                          many=False,
                          context={'request': request})

        data = ser.data
        return Response(data=data)


class Test4View(APIView):

    def get(self, request: Request, *args, **kwargs):
        stus = Student.objects.all()
        ser = StudentSeri(instance=stus,
                          many=True,
                          context={'request': request})

        data = ser.data

        return Response(data=data)
