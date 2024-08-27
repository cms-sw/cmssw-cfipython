import FWCore.ParameterSet.Config as cms

def FFTPF4CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF4CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
