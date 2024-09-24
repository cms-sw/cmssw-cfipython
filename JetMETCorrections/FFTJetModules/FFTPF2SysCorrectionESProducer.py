import FWCore.ParameterSet.Config as cms

def FFTPF2SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTPF2SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod