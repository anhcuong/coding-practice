-- 1.1
-- Table: users

-- id, mobile_number, created_at

-- q1: Create a table which list down all users with the same mobile_number
-- Eg: user_id_1, user_id_2, mobile_number
-- Dont list down duplicate rows: 1, 2, +65123458 == 2, 1, +65123458

SELECT
	u1.id AS user_id_1,
  u2.id AS user_id_2,
  u1.mobile_number AS mobile_number
FROM users AS u1
LEFT JOIN users AS u2
       ON u1.mobile_number = u2.mobile_number
WHERE u1.id < u2.id -- Filter the duplicate


-- 1.2
-- Table: users

-- id, created_at

-- Find all users who joined before that user
-- Eg: given_user_id, joined_before_user_id
SELECT
  u2.id AS given_user_id,
  u1.id AS joined_before_user_id
FROM users AS u1
LEFT JOIN users AS u2
       ON u1.created_at < u2.created_at


-- 1.3
-- Table: users

-- id, created_at

-- Given an user_id, count all users who joined before and count all users who joined after that user
-- Eg: given_user_id, total_user_joined_before, total_user_joined_after
SELECT
  u1.id AS given_user_id,
  SUM(CASE WHEN u2.created_at < u1.created_at THEN 1 ELSE 0 END) AS total_user_joined_before,
  SUM(CASE WHEN u2.created_at > u1.created_at THEN 1 ELSE 0 END) AS total_user_joined_after
FROM users AS u1
LEFT JOIN users AS u2
       ON 1 = 1  -- Cross Join
WHERE u1.id <> u2.id  -- Remove duplicate
GROUP BY 1
