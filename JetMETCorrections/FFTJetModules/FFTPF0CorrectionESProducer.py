import FWCore.ParameterSet.Config as cms

def FFTPF0CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF0CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
