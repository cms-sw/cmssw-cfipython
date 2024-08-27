import FWCore.ParameterSet.Config as cms

def FFTCHS0SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS0SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
