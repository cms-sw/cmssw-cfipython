import FWCore.ParameterSet.Config as cms

def FFTLUT6TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT6TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
