import FWCore.ParameterSet.Config as cms

def FFTPFCHS2CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPFCHS2CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
