import FWCore.ParameterSet.Config as cms

def FFTLUT3TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT3TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
