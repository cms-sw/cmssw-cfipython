import FWCore.ParameterSet.Config as cms

def FFTLUT12TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT12TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
