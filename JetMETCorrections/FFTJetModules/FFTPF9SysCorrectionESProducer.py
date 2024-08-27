import FWCore.ParameterSet.Config as cms

def FFTPF9SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF9SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
