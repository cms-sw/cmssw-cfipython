import FWCore.ParameterSet.Config as cms

def JetProbabilityESProducer(**kwargs):
  mod = cms.ESProducer('JetProbabilityESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
