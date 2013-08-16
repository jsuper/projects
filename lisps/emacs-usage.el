;;This is the scratch buffer

;; test writing file

(setq java-mode-data-file
      (expand-file-name ".java-mode-data.el"
			user-emacs-directory))

;;file exist or not
(file-exists-p java-mode-data-file)

;;open file but not switch to buffer
(find-file-noselect java-mode-data-file)

;; insert string to buffer
(defun test-insert ()
  (end-of-buffer)
  (insert "hello world"))
(test-insert)

;; hash demo
(setq my-hash (make-hash-table :test 'equal))
(puthash "joe" "192" my-hash)
(gethash "joe" my-hash)

(defun get-user-eclim-directory ()
  (let ((eclim-root (read-string "Enter your eclim root folder:")))
    (while (not (file-exists-p eclim-root))
      (set 'eclim-root (read-string "Enter your eclim root folder:")))
    (message eclim-root)))

(get-user-eclim-directory)
