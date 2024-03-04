import FWCore.ParameterSet.Config as cms

def FFTPF4SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF4SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
