DROP TABLE IF EXISTS user_key_space.public_keys;
CREATE TABLE user_key_space.public_keys (
  userid text PRIMARY KEY,
  cert_string  text
);
