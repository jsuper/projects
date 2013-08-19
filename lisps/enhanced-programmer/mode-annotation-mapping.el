;;mapping the annotation related data

(setq mode-annotation-data 
      '(
	(:name "emacs-lisp-mode"
	       :support-block-annotation nil
	       :annotation-char ";")
	
	(:name "java-mode"
	       :support-block-annotation t
	       :start-block-char "/*"
	       :end-block-char "*/"
	       :annotation-char "//")))

(defun select (selector-fn)
  (remove-if-not selector-fn mode-annotation-data))

(defun mode-name-selector (name)
  #'(lambda (mdata) (equal (getf mdata :name) name)))

(defun select-by-name (name)
  (first (select (mode-name-selector name))))

(provide 'mode-annotation-data)
