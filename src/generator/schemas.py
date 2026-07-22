from pydantic import BaseModel, HttpUrl, Field
from typing import Optional


class Seo(BaseModel):
    title: str
    description: str
    domain: str
    og_image: str
    og_image_width: str
    og_image_height: str
    og_image_type: str
    og_image_alt: str
    author: str
    theme_color: str
    locale: str
    favicon: str


class Hero(BaseModel):
    title: str
    subtitle: str
    author: str


class About(BaseModel):
    heading: str
    cover: str
    cover_alt: str
    paragraphs: list[str]
    signoff: str


class AuthorSection(BaseModel):
    name: str
    photo: str
    photo_alt: str
    paragraphs: list[str]


class SocialLink(BaseModel):
    url: str
    aria_label: str
    svg: str


class Social(BaseModel):
    heading: str
    links: list[SocialLink]


class ContactItem(BaseModel):
    type: str
    icon: str
    label: str
    url: str


class Contact(BaseModel):
    heading: str
    items: list[ContactItem]


class Footer(BaseModel):
    copyright_year: str
    developed_by: str
    developer_url: str


class Livro(BaseModel):
    seo: Seo
    isbn: str
    pdf_download: str
    youtube_id: str
    topbar_title: str
    hero: Hero
    about: About
    author: AuthorSection
    social: Social
    contact: Contact
    footer: Footer
