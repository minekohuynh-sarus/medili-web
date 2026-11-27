// Trang Tài khoản: chị chủ đặt lại mật khẩu, khoá, mở khoá, xóa tài khoản nhân viên.
(() => {
  const ask = { khoa: 'Khoá tài khoản này? Người đó bị đăng xuất ngay và không đăng nhập được nữa.', mo: 'Mở khoá tài khoản này?', xoa: 'Xóa hẳn tài khoản này?' };
  document.addEventListener('click', async e => {
    const b = e.target.closest('[data-tk]'); if (!b) return;
    const u = b.closest('tr').dataset.u, viec = b.dataset.tk, d = { u, viec };
    if (viec === 'mk') {
      const pw = prompt('Mật khẩu mới cho ' + u + ' (ít nhất 10 ký tự). Chị gửi mật khẩu này cho nhân viên qua Zalo riêng:');
      if (pw === null) return;
      if (pw.length < 10) { QT.toast('Mật khẩu cần ít nhất 10 ký tự.', true); return }
      d.pw = pw;
    } else if (!confirm(ask[viec])) return;
    QT.busy(b, true);
    try { const j = await QT.api('tk-sua', d); QT.toast(j.bao || 'Xong.'); setTimeout(() => location.reload(), 900) }
    catch (err) { QT.toast(err.message, true) }
    finally { QT.busy(b, false) }
  });
})();
