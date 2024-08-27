import FWCore.ParameterSet.Config as cms

def FFTLUT14TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT14TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
