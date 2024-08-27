import FWCore.ParameterSet.Config as cms

def FFTLUT4TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT4TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
