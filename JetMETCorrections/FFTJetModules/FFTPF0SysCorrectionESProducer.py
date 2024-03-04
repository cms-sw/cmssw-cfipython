import FWCore.ParameterSet.Config as cms

def FFTPF0SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF0SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
