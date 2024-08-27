import FWCore.ParameterSet.Config as cms

def FFTLUT11TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT11TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
