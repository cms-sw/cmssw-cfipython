import FWCore.ParameterSet.Config as cms

def FFTPF1SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPF1SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
