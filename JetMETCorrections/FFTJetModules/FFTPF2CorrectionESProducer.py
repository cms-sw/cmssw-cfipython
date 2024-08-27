import FWCore.ParameterSet.Config as cms

def FFTPF2CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF2CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
