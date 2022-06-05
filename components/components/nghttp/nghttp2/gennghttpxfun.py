#!/usr/bin/env python

from gentokenlookup import gentokenlookup

OPTIONS = [
    "private-key-file",
    "private-key-passwd-file",
    "certificate-file",
    "dh-param-file",
    "subcert",
    "backend",
    "frontend",
    "workers",
    "http2-max-concurrent-streams",
    "log-level",
    "daemon",
    "http2-proxy",
    "http2-bridge",
    "client-proxy",
    "add-x-forwarded-for",
    "strip-incoming-x-forwarded-for",
    "no-via",
    "frontend-http2-read-timeout",
    "frontend-read-timeout",
    "frontend-write-timeout",
    "backend-read-timeout",
    "backend-write-timeout",
    "stream-read-timeout",
    "stream-write-timeout",
    "accesslog-file",
    "accesslog-syslog",
    "accesslog-format",
    "errorlog-file",
    "errorlog-syslog",
    "backend-keep-alive-timeout",
    "frontend-http2-window-bits",
    "backend-http2-window-bits",
    "frontend-http2-connection-window-bits",
    "backend-http2-connection-window-bits",
    "frontend-no-tls",
    "backend-no-tls",
    "backend-tls-sni-field",
    "pid-file",
    "user",
    "syslog-facility",
    "backlog",
    "ciphers",
    "client",
    "insecure",
    "cacert",
    "backend-ipv4",
    "backend-ipv6",
    "backend-http-proxy-uri",
    "read-rate",
    "read-burst",
    "write-rate",
    "write-burst",
    "worker-read-rate",
    "worker-read-burst",
    "worker-write-rate",
    "worker-write-burst",
    "npn-list",
    "tls-proto-list",
    "verify-client",
    "verify-client-cacert",
    "client-private-key-file",
    "client-cert-file",
    "frontend-http2-dump-request-header",
    "frontend-http2-dump-response-header",
    "http2-no-cookie-crumbling",
    "frontend-frame-debug",
    "padding",
    "altsvc",
    "add-request-header",
    "add-response-header",
    "worker-frontend-connections",
    "no-location-rewrite",
    "no-host-rewrite",
    "backend-http1-connections-per-host",
    "backend-http1-connections-per-frontend",
    "listener-disable-timeout",
    "tls-ticket-key-file",
    "rlimit-nofile",
    "backend-request-buffer",
    "backend-response-buffer",
    "no-server-push",
    "backend-http2-connections-per-worker",
    "fetch-ocsp-response-file",
    "ocsp-update-interval",
    "no-ocsp",
    "include",
    "tls-ticket-key-cipher",
    "host-rewrite",
    "tls-session-cache-memcached",
    "tls-session-cache-memcached-tls",
    "tls-ticket-key-memcached",
    "tls-ticket-key-memcached-interval",
    "tls-ticket-key-memcached-max-retry",
    "tls-ticket-key-memcached-max-fail",
    "mruby-file",
    "accept-proxy-protocol",
    "conf",
    "fastopen",
    "tls-dyn-rec-warmup-threshold",
    "tls-dyn-rec-idle-timeout",
    "add-forwarded",
    "strip-incoming-forwarded",
    "forwarded-by",
    "forwarded-for",
    "response-header-field-buffer",
    "max-response-header-fields",
    "request-header-field-buffer",
    "max-request-header-fields",
    "header-field-buffer",
    "max-header-fields",
    "no-http2-cipher-black-list",
    "backend-http1-tls",
    "tls-session-cache-memcached-cert-file",
    "tls-session-cache-memcached-private-key-file",
    "tls-session-cache-memcached-address-family",
    "tls-ticket-key-memcached-tls",
    "tls-ticket-key-memcached-cert-file",
    "tls-ticket-key-memcached-private-key-file",
    "tls-ticket-key-memcached-address-family",
    "backend-address-family",
    "frontend-http2-max-concurrent-streams",
    "backend-http2-max-concurrent-streams",
    "backend-connections-per-frontend",
    "backend-tls",
    "backend-connections-per-host",
    "error-page",
    "no-kqueue",
    "frontend-http2-settings-timeout",
    "backend-http2-settings-timeout",
    "api-max-request-body",
    "backend-max-backoff",
    "server-name",
    "no-server-rewrite",
    "frontend-http2-optimize-write-buffer-size",
    "frontend-http2-optimize-window-size",
    "frontend-http2-window-size",
    "frontend-http2-connection-window-size",
    "backend-http2-window-size",
    "backend-http2-connection-window-size",
    "frontend-http2-encoder-dynamic-table-size",
    "frontend-http2-decoder-dynamic-table-size",
    "backend-http2-encoder-dynamic-table-size",
    "backend-http2-decoder-dynamic-table-size",
    "ecdh-curves",
    "tls-sct-dir",
    "backend-connect-timeout",
    "dns-cache-timeout",
    "dns-lookup-timeout",
    "dns-max-try",
    "frontend-keep-alive-timeout",
    "psk-secrets",
    "client-psk-secrets",
    "client-no-http2-cipher-black-list",
    "client-ciphers",
    "accesslog-write-early",
    "tls-min-proto-version",
    "tls-max-proto-version",
    "redirect-https-port",
    "frontend-max-requests",
    "single-thread",
    "single-process",
    "no-add-x-forwarded-proto",
    "no-strip-incoming-x-forwarded-proto",
    "ocsp-startup",
    "no-verify-ocsp",
    "verify-client-tolerate-expired",
    "ignore-per-pattern-mruby-error",
    "tls-no-postpone-early-data",
    "tls-max-early-data",
    "tls13-ciphers",
    "tls13-client-ciphers",
    "no-strip-incoming-early-data",
]

LOGVARS = [
    "remote_addr",
    "time_local",
    "time_iso8601",
    "request",
    "status",
    "body_bytes_sent",
    "remote_port",
    "server_port",
    "request_time",
    "pid",
    "alpn",
    "ssl_cipher",
    "ssl_protocol",
    "ssl_session_id",
    "ssl_session_reused",
    "tls_cipher",
    "tls_protocol",
    "tls_session_id",
    "tls_session_reused",
    "tls_sni",
    "tls_client_fingerprint_sha256",
    "tls_client_fingerprint_sha1",
    "tls_client_subject_name",
    "tls_client_issuer_name",
    "tls_client_serial",
    "backend_host",
    "backend_port",
]

if __name__ == '__main__':
    gentokenlookup(OPTIONS, 'SHRPX_OPTID_', value_type='char', comp_fun='util::strieq_l')
    gentokenlookup(LOGVARS, 'LogFragmentType::', value_type='char', comp_fun='util::strieq_l', return_type='LogFragmentType', fail_value='LogFragmentType::NONE')
