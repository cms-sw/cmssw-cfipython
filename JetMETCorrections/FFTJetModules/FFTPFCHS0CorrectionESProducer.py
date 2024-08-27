import FWCore.ParameterSet.Config as cms

def FFTPFCHS0CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPFCHS0CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
