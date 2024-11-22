import FWCore.ParameterSet.Config as cms

def FFTPFCHS1CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPFCHS1CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
