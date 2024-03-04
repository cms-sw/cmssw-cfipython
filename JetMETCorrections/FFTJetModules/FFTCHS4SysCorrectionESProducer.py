import FWCore.ParameterSet.Config as cms

def FFTCHS4SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS4SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
