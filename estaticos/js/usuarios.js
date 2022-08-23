/*
 * Copyright (c) 2021. Hexagoon. Criador: Fabricio Gatto Lourençone. Todos os direitos reservados.
 */

async function excluirUsuario(){
    const id = window.event.target.id.replace('ue', '');
    const token = localStorage.getItem("jwt");

    const response = await fetch(`${baseUrl}/usuario/${id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    if (!response.ok) {
        const message = `Um erro ocorreu ${response.status}`;
        throw new Error(message);
    }
    if (response.status === 200){
        const nome = document.querySelector(`#u${id}`)
        nome.style.textDecoration = 'line-through';
    }

}

async function desativarUsuario(){
    const id = window.event.target.id.replace('ud', '');
    const token = localStorage.getItem("jwt");

    const response = await fetch(`${baseUrl}/usuario/${id}/inactivate`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    if (!response.ok) {
        const message = `Um erro ocorreu ${response.status}`;
        throw new Error(message);
    }
    if (response.status === 200){
        const nome = document.querySelector(`#ua${id}`)
        nome.textContent = 'Não';
    }

}

async function ativarUsuario() {
    const id = window.event.target.id.replace('ut', '');
    const token = localStorage.getItem("jwt");

    const email = document.querySelector(`#e${id}`).innerText;

    const response = await fetch(`${baseUrl}/autenticacao/recuperar`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            "email": email
        })
    });

    if (!response.ok) {
        const message = `Um erro ocorreu ${response.status}`;
        throw new Error(message);
    }
    if (response.status === 202) {
        const nome = document.querySelector(`#ua${id}`);
        nome.textContent = 'Sim';
    }
}

async function showFormUsuario(){
        const form = document.querySelector('#formCriaUsuario');
        form.style.display = 'table';
        const button = document.querySelector('#buttonCriaUsuario');
        button.style.display = 'none';
}

async function submeterUsuario(){

    const token = localStorage.getItem("jwt");

    const email = document.querySelector('#email').value;
    const senha = document.querySelector('#senha').value;
    const nome = document.querySelector('#nome').value;

    const create_response = await fetch(`${baseUrl}/usuario`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            "email": email,
            "senha": senha,
            "nome": nome
        })
    });

    if (!create_response.ok) {
        const response = await create_response.json();
        let error = 'Erro na criação do usuário.';
        if (typeof response['detail'] === 'string' ){
            error = response['detail'];
        } else {
            error = response['detail'][0]['msg'];
        }
        const p = document.createElement("p");
        const alerta = document.createTextNode(`Falha na autenticação! ${error}`);
        p.appendChild(alerta); //adiciona o nó de texto à nova div criada
        document.querySelector('#formCriaUsuario').appendChild(p);
    }

    if (create_response.status === 201) {
        const response = await create_response.json();
        const p = document.createElement("p");
        const alerta = document.createTextNode(`Usuário id ${response['id']} criado com sucesso`);
        p.appendChild(alerta); //adiciona o nó de texto à nova div criada
        document.querySelector('#formCriaUsuario').appendChild(p);

        const user_layout = document.querySelector('table[layout=usuario]');
        const user_clone = user_layout.cloneNode(true);
        let id = user_clone.querySelector('table  tr:first-child td:nth-child(2)').getAttribute('id');
        id = id.replace('u', '');
        user_clone.querySelector(`#u${id}`).innerText = response['nome'];
        user_clone.querySelector(`#u${id}`).setAttribute('id', `u${response['id']}`);
        user_clone.querySelector(`#e${id}`).innerText = response['email'];
        user_clone.querySelector(`#e${id}`).setAttribute('id', `e${response['id']}`);
        user_clone.querySelector(`#ua${id}`).innerText = 'Sim';
        user_clone.querySelector(`#ua${id}`).setAttribute('id', `ua${response['id']}`);
        user_clone.querySelector(`#ue${id}`).setAttribute('id', `ue${response['id']}`);
        user_clone.querySelector(`#ud${id}`).setAttribute('id', `ud${response['id']}`);
        user_clone.querySelector(`#ut${id}`).setAttribute('id', `ut${response['id']}`);
        document.querySelector('#navigation').appendChild(user_clone);
    }
}

async function adicionarPerfil(){
    const id = window.event.target.id.replace('pa', '');
    const role_id = document.querySelector(`#psa${id}`).selectedOptions[0].value;
    const token = localStorage.getItem("jwt");

    const response = await fetch(`${baseUrl}/as_usuario_role/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            "usuario_id": id,
            "role_id": role_id
        })
    });

    if (!response.ok) {
        const message = `Um erro ocorreu ${response.status}`;
        throw new Error(message);
    }
    if (response.status === 201){
        // adiciona o perfil na lista de perfis
        const perfis = document.querySelector(`#p${id}`);
        perfis.innerText = perfis.innerText + " " + document.querySelector(`#psa${id}`).selectedOptions[0].innerText;

        // alterar o id do perfil na opção para pode ser excluído/adicionado novamente.
//        const opcaoPerfil = document.querySelector(`select[name=perfisRemover] option[#psr${id}`);
//        opcaoPerfil.value = response['role_id'];
//        opcaoPerfil.id = `op${response['role_id']}`;

    }

}

async function excluirPerfil(){
    const id = window.event.target.id.replace('pr', '');
    const role_id = document.querySelector(`#psr${id}`).selectedOptions[0].value;
    const token = localStorage.getItem("jwt");

    const response = await fetch(`${baseUrl}/as_usuario_role/${role_id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    if (!response.ok) {
        const message = `Um erro ocorreu ${response.status}`;
        throw new Error(message);
    }
    if (response.status === 200){
        const perfis = document.querySelector(`#p${id}`);
        perfis.innerText = perfis.innerText.replace(document.querySelector(`#psr${id}`).selectedOptions[0].innerText, "");
    }

}
