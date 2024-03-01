{
    'targets': [
        {
            'target_name': 'node-tspsolver',
            'include_dirs': [
                '<!(node -e "require(\'nan\')")'
            ],
            'cflags': ['-std=c++17'],
            'sources': [
                'src/addon.cpp',
                'src/tsp_v8.cpp',
                'src/tsp.cpp'
            ],
            'conditions': [
                ['OS!="win"', {
                    'cflags+': ['-std=c++17'],
                    'cflags_c+': ['-std=c++17'],
                    'cflags_cc+': ['-std=c++17'],
                }],
                ['OS=="mac"', {
                    'xcode_settings': {
                        'OTHER_CPLUSPLUSFLAGS': ['-std=c++17', '-stdlib=libc++'],
                        'OTHER_LDFLAGS': ['-stdlib=libc++'],
                        'MACOSX_DEPLOYMENT_TARGET': '11.6'
                    }
                }]
            ]
        }
    ]
}
