Name:		kokoro-voice-zm_yunxia
Version:	1.0
Release:	1
Summary:	Mandarin male Kokoro voice zm_yunxia
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-zh
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/zm_yunxia.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Mandarin grapheme-to-phoneme support is not part of python-misaki yet, so synthesis with this voice stops until that support is packaged.
Select it with: kokoro -m zm_yunxia

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/zm_yunxia.pt

%files
%{_datadir}/kokoro/voices/zm_yunxia.pt
