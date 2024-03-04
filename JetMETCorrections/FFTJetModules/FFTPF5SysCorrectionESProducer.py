import FWCore.ParameterSet.Config as cms

def FFTPF5SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF5SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
