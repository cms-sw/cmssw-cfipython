import FWCore.ParameterSet.Config as cms

def FFTPFCHS1CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPFCHS1CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
