def includeme(config):
    """Menambahkan rute ke konfigurasi."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    # Pastikan rute 'home' sudah terdefinisi
    config.add_route('home', '/')  # Tambahkan baris ini
    
    # Rute lainnya
    config.add_route('matakuliah_list', '/api/matakuliah', request_method='GET')
    config.add_route('matakuliah_detail', '/api/matakuliah/{id}', request_method='GET')
    config.add_route('matakuliah_add', '/api/matakuliah', request_method='POST')
    config.add_route('matakuliah_update', '/api/matakuliah/{id}', request_method='PUT')
    config.add_route('matakuliah_delete', '/api/matakuliah/{id}', request_method='DELETE')
