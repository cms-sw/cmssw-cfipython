import FWCore.ParameterSet.Config as cms

def FFTPF7SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF7SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
