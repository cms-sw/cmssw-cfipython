import FWCore.ParameterSet.Config as cms

def FFTLUT2TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT2TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
