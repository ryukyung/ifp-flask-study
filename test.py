{% if user.is_authenticated %}
<li class="nav-item">
  <a class="nav-link px-lg-3 py-3 py-lg-4" style="color: red" href="#"
    >welcome, {{ user.username }}!
  </a>
</li>
<li class="nav-item">
  <a
    class="nav-link px-lg-3 py-3 py-lg-4"
    style="color: red"
    href="{{ url_for('auth.logout') }}"
    >Logout</a
  >
</li>
{% else %} 
<li class="nav-item">
  <a class="nav-link px-lg-3 py-3 py-lg-4" href="{{ url_for('auth.signup') }}"
    >Sign Up</a
  >
</li>
<li class="nav-item">
  <a class="nav-link px-lg-3 py-3 py-lg-4" href="{{ url_for('auth.login') }}"
    >Login</a
  >
</li>
{% endif %}
