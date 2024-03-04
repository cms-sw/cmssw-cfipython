import FWCore.ParameterSet.Config as cms

def FFTLUT13TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT13TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
