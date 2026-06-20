from flask import Blueprint, render_template_string
auth_bp = Blueprint("auth", __name__)
_PLACEHOLDER = """
{% extends "layouts/base.html" %}
{% block content %}
<section class="glass p-5 text-center">
  <h1 class="section-title">🔐 {{ title }}</h1>
  <p class="text-muted">Authentication is coming soon. This route is reserved for future expansion.</p>
</section>
{% endblock %}
"""
@auth_bp.route("/login")
def login():
    return render_template_string(_PLACEHOLDER, title="Login")
@auth_bp.route("/register")
def register():
    return render_template_string(_PLACEHOLDER, title="Register")