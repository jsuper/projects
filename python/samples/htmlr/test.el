;;This is the scratch buffer

(with-current-buffer (get-buffer "new.txt")
  (insert (propertize " bold" 'face '(:family "helv" :height 2.0 :weight bold)))
  )

(require 'cl)
(require 'cl-lib)

(with-current-buffer (get-buffer "html.html")
  (goto-char (point-min))
  (while (search-forward-regexp "<\\([[:word:]]+\\)" nil 'noerror)
    (let* ((tag-name (match-string-no-properties 1))
	   (tag-start (point))
	   (tag-end (when (search-forward ">" nil 'noerror 1)
		      (point))))
      (when (and tag-name tag-start tag-end)
	(message "%s%s%s" "<" tag-name (buffer-substring-no-properties tag-start tag-end)))      
      )))
