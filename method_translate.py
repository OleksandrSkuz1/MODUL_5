text = "Python  Ptop"

print(text.translate({80: "hello"}))        # даний метод translate, знайшов числове входження символу (P=80 табл. ASCI) i замінив його на ("hello") 
                                            # в результаті отримаємо замість Python - helloython (P-hello)

                                            
print(text.translate({ord("P"): "hello"}))  # або за допомогою ord                                        