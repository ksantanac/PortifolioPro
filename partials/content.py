import flet as ft


class ProjectItem(ft.UserControl):

    def __init__(self, title: str, description: str, url: str, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.url = url

    def build(self):
        return ft.Container(
            padding=ft.padding.all(30),
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            content=ft.Column(
                controls=[
                    ft.Text(value=self.title, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                    ft.Text(value=self.description),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(value="VER AO VIVO", theme_style=ft.TextThemeStyle.BODY_LARGE),
                                ft.Icon(name=ft.icons.ARROW_FORWARD_IOS, size=14, color=ft.colors.PRIMARY)
                            ],
                            tight=True
                        ),
                        url=self.url,
                    )
                ]
            )
        )


class MainContent(ft.UserControl):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True

    def build(self):
        banner = ft.Container(
            shadow=ft.BoxShadow(
                color=ft.colors.ON_BACKGROUND,
                offset=ft.Offset(x=0, y=-60),
                spread_radius=-30
            ),
            image_src="images/teste.jpg",
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            image_opacity=0.5,
            bgcolor=ft.colors.BACKGROUND,
            margin=ft.margin.only(top=30),
            content=ft.ResponsiveRow(
                columns=12,
                vertical_alignment=ft.CrossAxisAlignment.END,
                controls=[
                    ft.Container(
                        col={"md": 12, "lg": 8},
                        padding=ft.padding.all(50),
                        content=ft.Column(
                            controls=[
                                ft.Text(value="Descubra meu Incrível Portfólio",
                                        theme_style=ft.TextThemeStyle.HEADLINE_LARGE),
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(text="<"),
                                        ft.TextSpan(text="code", style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                        ft.TextSpan(text=">"),

                                        ft.TextSpan(
                                            text="Eu desenvolvo aplicativos IOS e Android, softwares para MacOS, Windows, Linux. Além de websites responsivos.",
                                            style=ft.TextStyle(color=ft.colors.WHITE),
                                        ),

                                        ft.TextSpan(text="</"),
                                        ft.TextSpan(text="code", style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                        ft.TextSpan(text=">"),
                                    ],
                                    theme_style=ft.TextThemeStyle.BODY_MEDIUM
                                ),
                                ft.ElevatedButton(
                                    bgcolor=ft.colors.PRIMARY,
                                    content=ft.Text(value="Explore agora", color=ft.colors.BLACK,
                                                    weight=ft.FontWeight.BOLD),
                                    url="https://www.linkedin.com/in/kaue-matheus-santana-9a24991b1/",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
                                )
                            ],
                            spacing=30,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ),

                    # ft.Container(
                    #     col={"md": 12, "lg": 4},
                    #     content=ft.Image(
                    #         src="images/teste_p.png",
                    #         width=20,
                    #         # scale=ft.Scale(scale=1.8, alignment=ft.alignment.bottom_center)
                    #     )
                    # )
                ]
            )
        )

        experience = ft.Container(
            padding=ft.padding.symmetric(vertical=20),
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Text(
                        col={"xs": 6, "md": 4},
                        spans=[
                            ft.TextSpan(
                                text="2 + ",
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight=ft.FontWeight.W_900,
                                    size=20
                                )
                            ),
                            ft.TextSpan(
                                text=" Anos de experiência",
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
                                    size=16
                                )
                            )
                        ]
                    ),

                    ft.Text(
                        col={"xs": 6, "md": 4},
                        spans=[
                            ft.TextSpan(
                                text="10 + ",
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight=ft.FontWeight.W_900,
                                    size=20
                                )
                            ),
                            ft.TextSpan(
                                text=" Projetos concluídos",
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
                                    size=16
                                )
                            )
                        ]
                    ),

                    ft.Text(
                        col={"xs": 6, "md": 4},
                        spans=[
                            ft.TextSpan(
                                text="7 + ",
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight=ft.FontWeight.W_900,
                                    size=20
                                )
                            ),
                            ft.TextSpan(
                                text=" Linguagens de domínio",
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
                                    size=16
                                )
                            )
                        ]
                    ),
                ]
            )
        )

        projects = ft.ResponsiveRow(
            columns=12,
            controls=[
                ProjectItem(
                    title="Site Pinterest",
                    description="Este é um projeto desenvolvido em Python utilizando Flask, HTML e CSS para criar um site semelhante ao Pinterest.",
                    url="https://github.com/ksantanac/PinterestFake",
                    col={"xs": 12, "md": 6, "lg": 4}
                ),
                ProjectItem(
                    title="ToDo App",
                    description="Aplicativo para gerenciamento de tarefas com integração ao banco de dados SQLite.",
                    url="",
                    col={"xs": 12, "md": 6, "lg": 4}
                ),

                ProjectItem(
                    title="Sistema de Login",
                    description="Sistema completo de autenticação de usuário com suporte a recuparação de senha e cadastro de novos usuários.",
                    url="",
                    col={"xs": 12, "md": 6, "lg": 4}
                ),

                ProjectItem(
                    title="Dashboard de Ações",
                    description="Construí um Dashboard a partir do zero, realizando a extração, transformação e carga"
                                " (ETL) de dados financeiros específicos de ações através de uma API.",
                    url="https://www.linkedin.com/feed/update/urn:li:activity:7151215789872754690/",
                    col={"xs": 12, "md": 6, "lg": 4}

                ),

                ProjectItem(
                    title="Sistema de Cadastro",
                    description="Sistema completo de cadastro oferece funcionalidades como busca automática "
                                "de CEP, calendário para seleção de datas, e geração de relatórios em PDF. Com ênfase "
                                "na eficiência e interatividade, otimiza o gerenciamento de clientes de forma intuitiva.",
                    url="https://www.linkedin.com/feed/update/urn:li:activity:7156024610256240641/",
                    col={"xs": 12, "md": 6, "lg": 4}

                ),

            ],
            spacing=30,
            run_spacing=30,
        )

        logos = ft.Container(
            padding=ft.padding.all(30),
            opacity=0.9,
            content=ft.ResponsiveRow(
                controls=[
                    ft.Image(
                        src="images/unifisa.png",
                        col={"xs": 6, "lg": 3, "xl": 3}
                    ),
                    ft.Image(
                        src="images/sodexo_logo.png",
                        col={"xs": 6, "lg": 3, "xl": 3}
                    ),
                    ft.Image(
                        src="images/metlife.png",
                        col={"xs": 6, "lg": 3, "xl": 3}
                    ),
                ],
                spacing=30,
                run_spacing=30,
            )
        )

        footer = ft.Container(
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            padding=ft.padding.all(30),
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Text(
                        col={"xs": 12, "md": 6},
                        value="© 2024 todos os direitos reservados",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                    ),

                    ft.Text(
                        col={"xs": 12, "md": 6},
                        spans=[
                            ft.TextSpan(text="Email: "),
                            ft.TextSpan(
                                text="kauesantana_13@hotmail.com",
                                url="mailto:kauesantana_13@hotmail.com"
                            )
                        ],
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                        text_align=ft.TextAlign.END
                    ),
                ]
            )
        )

        def sections_title(title: str):
            return ft.Container(
                padding=ft.padding.all(20),
                content=ft.Text(value=title, theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)
            )

        return ft.Container(
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    banner,
                    experience,
                    sections_title(title="Projetos"),
                    projects,
                    sections_title(title="Experiências"),
                    logos,
                    footer,
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
            padding=ft.padding.all(30)
        )
