import FWCore.ParameterSet.Config as cms

def FFTPFCHS0CorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPFCHS0CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
