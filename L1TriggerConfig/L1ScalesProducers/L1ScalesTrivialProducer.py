import FWCore.ParameterSet.Config as cms

def L1ScalesTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1ScalesTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
