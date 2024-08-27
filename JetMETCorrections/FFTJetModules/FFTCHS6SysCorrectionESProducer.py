import FWCore.ParameterSet.Config as cms

def FFTCHS6SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS6SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
