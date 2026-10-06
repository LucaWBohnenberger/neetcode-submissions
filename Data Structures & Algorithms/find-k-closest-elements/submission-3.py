class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = 0, len(arr) - k

        
        while L < R:
            mid = (L + R) // 2
            
        
            if x - arr[mid] > arr[mid + k] - x:
                L = mid + 1
            else:
                # Se a distância para a esquerda for menor ou igual,
                # significa que esta janela [mid, ..., mid + k] é uma
                # boa candidata (ou está muito à direita).
                # Movemos o ponteiro da direita (R) para 'mid'.
                # (Lembre-se do desempate: 'arr[mid]' é menor que 'arr[mid+k]',
                # então se a distância for igual, preferimos 'mid')
                R = mid

        # O loop termina quando L == R, e 'L' será o índice
        # inicial da melhor janela de tamanho k.
        
        # Retornamos a sub-array que começa em L e tem tamanho k.
        return arr[L : L + k]
            
