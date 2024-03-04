import FWCore.ParameterSet.Config as cms

def FFTLUT10TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT10TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
