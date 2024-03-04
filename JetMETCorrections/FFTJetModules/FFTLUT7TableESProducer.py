import FWCore.ParameterSet.Config as cms

def FFTLUT7TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT7TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
