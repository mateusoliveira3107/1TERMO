# 🖥️ Curso: Sistemas Operacionais

## 📌 Conteúdo Programático Geral
* Conceitos fundamentais e arquitetura de SO.
* Gerenciamento de processos, memória e arquivos.
* Virtualização e ambientes isolados.
* Operação de sistemas via interface de linha de comando.

---

## 🗲 1. Fundamentos de Sistemas Operacionais

### O que é um SO?
* Intermediário entre o hardware e os programas aplicativos.
* Gerenciador de recursos (CPU, memória, dispositivos de E/S).

### Núcleo (Kernel)
* Parte central do sistema operacional.
* Responsável pelo acesso seguro ao hardware.
* **Modo Usuário:** Execução de aplicativos comuns com privilégios limitados.
* **Modo Kernel:** Execução de instruções críticas do sistema.

---

## 🔲 2. Virtualização e Máquinas Virtuais (VMs)

### Conceitos de Virtualização
* Execução de múltiplos SOs isolados no mesmo hardware.
* **Hipervisor (VMM):** Software que gerencia as máquinas virtuais.
* **Tipo 1 (Nativo):** Executa direto no hardware (Ex: VMware ESXi, Proxmox).
* **Tipo 2 (Hospedado):** Executa sobre outro SO (Ex: VirtualBox, VMware Workstation).

### Benefícios das VMs
* Isolamento completo de ambientes para testes seguros.
* Otimização e redução de custos com servidores físicos.
* Facilidade para clonagem e backup de sistemas inteiros.

---

## ⌨️ 3. Interface de Linha de Comando (CLI / Prompt)

### Prompt de Comando (Windows) vs. Terminal (Linux)
* **CLI:** Interação textual rápida e eficiente com o SO.
* **Scripts:** Automação de tarefas repetitivas do sistema.

### Comandos Essenciais de Navegação e Arquivos
* `cd`: Altera o diretório atual de trabalho.
* `dir` (Windows) / `ls` (Linux): Lista o conteúdo da pasta.
* `mkdir`: Cria um novo diretório no sistema.
* `copy` (Windows) / `cp` (Linux): Copia arquivos ou pastas.
* `del` (Windows) / `rm` (Linux): Remove arquivos do disco.

### Comandos de Rede e Diagnóstico
* `ping`: Testa a conectividade com um host de rede.
* `ipconfig` (Windows) / `ip a` (Linux): Exibe detalhes de rede.
* `tasklist` (Windows) / `ps` (Linux): Lista processos em execução.

---

## 🔄 4. Gerenciamento de Processos e Memória

### Processos e Threads
* **Processo:** Programa em execução com memória própria alocada.
* **Thread:** Subdivisão de um processo que executa tarefas em paralelo.
* **Escalonamento de CPU:** Algoritmos que decidem qual processo usa a CPU.

### Memória RAM e Virtual
* **Memória RAM:** Espaço volátil de alta velocidade para o processador.
* **Memória Virtual (Paging/Swap):** Uso do disco rígido para estender a RAM.

---

## 📁 5. Sistemas de Arquivos e Permissões

### Organização de Dados
* Formas como o SO armazena, organiza e nomeia arquivos.
* **Windows:** Uso comum de sistemas NTFS e FAT32.
* **Linux:** Uso comum de sistemas EXT4.
* **Permissões:** Controle de acesso para leitura, escrita e execução.
