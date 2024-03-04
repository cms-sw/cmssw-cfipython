import FWCore.ParameterSet.Config as cms

def L1GtParametersTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1GtParametersTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
