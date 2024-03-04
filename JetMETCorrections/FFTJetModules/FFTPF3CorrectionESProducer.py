import FWCore.ParameterSet.Config as cms

def FFTPF3CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF3CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
