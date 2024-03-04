import FWCore.ParameterSet.Config as cms

def DTConfigTrivialProducer(**kwargs):
  mod = cms.ESProducer('DTConfigTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
