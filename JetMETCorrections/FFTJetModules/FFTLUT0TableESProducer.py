import FWCore.ParameterSet.Config as cms

def FFTLUT0TableESProducer(**kwargs):
  mod = cms.ESProducer('FFTLUT0TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
