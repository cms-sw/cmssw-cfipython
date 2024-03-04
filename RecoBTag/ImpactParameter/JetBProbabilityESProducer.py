import FWCore.ParameterSet.Config as cms

def JetBProbabilityESProducer(**kwargs):
  mod = cms.ESProducer('JetBProbabilityESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
