import FWCore.ParameterSet.Config as cms

def FFTCHS9SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS9SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
