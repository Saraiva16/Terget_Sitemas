#4)
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
out = 19849.53
soma = (sp+rj+mg+es+out)

print(f"O faturamento total é de R${soma}")

f_sp = (sp*100)/soma
print(f"O Estado de São Paulo representa, aproximadamente, {f_sp:.2f}% do faturamento total.")

f_rj = (rj*100)/soma
print(f"O Estado do Rio de Janeiro representa, aproximadamente, {f_rj:.2f}% do faturamento total.")

f_mg = (mg*100)/soma
print(f"O Estado de Minas Gerais representa, aproximadamente, {f_mg:.2f}% do faturamento total.")

f_es = (es*100)/soma
print(f"O Estado do Espírito Santo representa, aproximadamente, {f_es:.2f}% do faturamento total.")

f_out = (out*100)/soma
print(f"Os demais estados representam, aproximadamente, {f_out:.2f}% do faturamento total.")