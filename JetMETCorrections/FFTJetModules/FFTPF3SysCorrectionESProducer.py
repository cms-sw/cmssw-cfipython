import FWCore.ParameterSet.Config as cms

def FFTPF3SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPF3SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
