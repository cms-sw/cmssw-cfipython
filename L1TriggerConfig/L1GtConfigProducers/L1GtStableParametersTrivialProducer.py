import FWCore.ParameterSet.Config as cms

def L1GtStableParametersTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1GtStableParametersTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
