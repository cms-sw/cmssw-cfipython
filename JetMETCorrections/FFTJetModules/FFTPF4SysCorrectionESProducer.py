import FWCore.ParameterSet.Config as cms

def FFTPF4SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPF4SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
