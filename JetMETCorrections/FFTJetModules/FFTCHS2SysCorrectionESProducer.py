import FWCore.ParameterSet.Config as cms

def FFTCHS2SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS2SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
