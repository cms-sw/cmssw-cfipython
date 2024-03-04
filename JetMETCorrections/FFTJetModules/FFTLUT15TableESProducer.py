import FWCore.ParameterSet.Config as cms

def FFTLUT15TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT15TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
