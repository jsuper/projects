;;enhanced function for programmer 
;; 1. mutil-line annotated
;;
;Test annotation
(require 'mode-annotation-data)

(defun annonate--current-line (mode-data)
  (print mode-data)
  (let ((ann-char (getf mode-data :annotation-char)))
    (message "ann-char %s" ann-char)
    (when ann-char
      (goto-char (line-beginning-position))
      (insert-string ann-char))))


(defun annotate--region (start-pos end-pos)
  (let ((mode-data (select-by-name (format "%s" major-mode)))
	(lines-count (count-lines start-pos end-pos)))
    (message "line count %d" lines-count)
    (if (getf mode-data :support-block-annotation)
	(progn
	  (goto-char start-pos)
	  (insert-string (getf mode-data :start-block-char))
	  (goto-char end-pos)
	  (insert-string (getf mode-data :end-block-char)))
      (if (equal 1 lines-count)
	  (annonate--current-line mode-data)
	(progn 
	  (setq current-line-pos start-pos)
	  (dotimes (i lines-count)
	    (goto-char current-line-pos)
	    (goto-char (line-beginning-position))
	    (insert-string (getf mode-data :annotation-char))
	    (setq current-line-pos (+ 1 (line-end-position)))
	    ))))))

(defun annotate-region () 
  (interactive)
  (annotate--region (region-beginning) (region-end)))

(global-set-key (kbd "M-p") 'annotate-region)
