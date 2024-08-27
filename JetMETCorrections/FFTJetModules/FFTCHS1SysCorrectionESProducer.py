import FWCore.ParameterSet.Config as cms

def FFTCHS1SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS1SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
