import FWCore.ParameterSet.Config as cms

def FFTLUT9TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT9TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
