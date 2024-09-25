import FWCore.ParameterSet.Config as cms

def FFTPFCHS2SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPFCHS2SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
