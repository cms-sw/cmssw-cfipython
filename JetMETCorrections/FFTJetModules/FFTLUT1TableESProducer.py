import FWCore.ParameterSet.Config as cms

def FFTLUT1TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT1TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
