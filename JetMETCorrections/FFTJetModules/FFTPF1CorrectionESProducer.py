import FWCore.ParameterSet.Config as cms

def FFTPF1CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF1CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
