import FWCore.ParameterSet.Config as cms

def FFTPF7SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPF7SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
