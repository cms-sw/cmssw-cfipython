import FWCore.ParameterSet.Config as cms

def FFTLUT8TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT8TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
