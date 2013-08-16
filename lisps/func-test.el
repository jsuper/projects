;; test function

(defun insert-after (list-ref inserted index)
  (push inserted (nthcdr index list-ref))
  list-ref)

(defun insert-before (list-ref argument)
  (insert-after list-ref argument 0))


;;; call an external program and show its ouput in minimal buffer
(defun call--process (program &rest args)
  (with-temp-buffer
    (setq arg-list 
	  (insert-before
	   (insert-before
	    (insert-before 
	     (insert-before args t) 
	     (current-buffer))
	    nil)
	   program))
    (apply 'call-process arg-list)
    (setq origin-print-escape-newlines print-escape-newlines)
    (setq print-escape-newlines nil)
    (message (buffer-substring-no-properties 1 (point-max)))))

(call--process "python" "c:/cygwin/tmp/hello.py")
(print 'helllo)

(print '(buffer-string))
