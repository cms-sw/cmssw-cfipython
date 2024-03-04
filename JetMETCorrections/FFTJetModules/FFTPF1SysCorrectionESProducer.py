import FWCore.ParameterSet.Config as cms

def FFTPF1SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF1SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
