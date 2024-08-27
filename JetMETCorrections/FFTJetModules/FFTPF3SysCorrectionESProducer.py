import FWCore.ParameterSet.Config as cms

def FFTPF3SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF3SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
