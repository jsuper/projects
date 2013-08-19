
(defun current-line ()
  (interactive)
  (let ((start-pos (line-beginning-position))
	(end-pos (line-end-position)))
    (message (buffer-substring start-pos end-pos))))

(defun region-data ()
  (message (buffer-substring (region-beginning region-end))))

(defun region-data ()
  (interactive)
  (setq region-string (buffer-substring (region-beginning) (region-end)))
  (message "line number %d" (line-number-at-pos (region-beginning)))
  (goto-char (point-max))
  (insert-string (concat 
		  "\n" 
		  region-string)))

(line-end-position)

(local-set-key (kbd "M-p") 'region-data)
(line-move 19)

;;; lines = count-lines(region-start, region-end)
;;; first-line-pos=region-start
;;; repeat lines
;;;    line-pos=line-pos(goto-char(first-line-pos))
;;    goto-char(begin-of-line)
;;    insert-string(";")
;;    goto-char(end-of-line+1)

(defun count--lines ()
  (interactive)
  (message "line cout : %d"
	   (count-lines (region-beginning)
			       (region-end))))

   
(debug-on-entry 'annonate-region)

(defun annonate-region ()
  (interactive)
  (let ((region-start (region-beginning))
	(region-end-pos (region-end))
	(line-count (count-lines (region-beginning)
				 (region-end))))
    (message "selected lines count is [%d]" line-count)
    (setq current-line-region (region-beginning))
    (dotimes (i line-count)
      (progn
	(goto-char current-line-region) 
	(goto-char (line-beginning-position))
	(insert-string ";")
	(setq current-line-region (+ 1 (line-end-position)))))))

(local-set-key (kbd "M-p") 'annonate-region)
