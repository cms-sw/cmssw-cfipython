import FWCore.ParameterSet.Config as cms

def FFTPFCHS2CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPFCHS2CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
