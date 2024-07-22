import FWCore.ParameterSet.Config as cms

def FFTPF6SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF6SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod