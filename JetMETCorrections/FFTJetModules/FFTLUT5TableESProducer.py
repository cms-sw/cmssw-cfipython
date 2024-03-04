import FWCore.ParameterSet.Config as cms

def FFTLUT5TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT5TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
