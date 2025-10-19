from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    """Bandeja de entrada - Mensajes recibidos"""
    mensajes_recibidos = Message.objects.filter(destinatario=request.user)
    no_leidos = mensajes_recibidos.filter(leido=False).count()
    return render(request, 'messenger/inbox.html', {
        'mensajes': mensajes_recibidos,
        'no_leidos': no_leidos
    })

@login_required
def sent(request):
    """Mensajes enviados"""
    mensajes_enviados = Message.objects.filter(remitente=request.user)
    return render(request, 'messenger/sent.html', {
        'mensajes': mensajes_enviados
    })

@login_required
def message_detail(request, pk):
    """Ver detalle de un mensaje"""
    mensaje = get_object_or_404(Message, pk=pk)
    
    # Verificar que el usuario sea el remitente o destinatario
    if request.user != mensaje.remitente and request.user != mensaje.destinatario:
        messages.error(request, 'No tienes permiso para ver este mensaje')
        return redirect('messenger:inbox')
    
    # Marcar como leído si es el destinatario
    if request.user == mensaje.destinatario and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    
    return render(request, 'messenger/message_detail.html', {'mensaje': mensaje})

@login_required
def compose(request, reply_to=None):
    """Crear nuevo mensaje"""
    initial_data = {}
    mensaje_original = None
    
    # Si es una respuesta, pre-llenar datos
    if reply_to:
        mensaje_original = get_object_or_404(Message, pk=reply_to)
        # Verificar que el usuario sea destinatario del mensaje original
        if request.user == mensaje_original.destinatario:
            initial_data['destinatario'] = mensaje_original.remitente.id
            initial_data['asunto'] = f'Re: {mensaje_original.asunto}' if not mensaje_original.asunto.startswith('Re:') else mensaje_original.asunto
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            messages.success(request, f'Mensaje enviado a {mensaje.destinatario.username}')
            return redirect('messenger:sent')
    else:
        form = MessageForm(initial=initial_data)
    
    return render(request, 'messenger/compose.html', {
        'form': form,
        'mensaje_original': mensaje_original
    })

@login_required
def delete_message(request, pk):
    """Borrar un mensaje"""
    mensaje = get_object_or_404(Message, pk=pk)
    
    # Solo el destinatario puede borrar mensajes recibidos
    if request.user != mensaje.destinatario:
        messages.error(request, 'No tienes permiso para borrar este mensaje')
        return redirect('messenger:inbox')
    
    if request.method == 'POST':
        mensaje.delete()
        messages.success(request, 'Mensaje eliminado')
        return redirect('messenger:inbox')
    
    return render(request, 'messenger/message_confirm_delete.html', {'mensaje': mensaje})
