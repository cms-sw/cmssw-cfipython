import FWCore.ParameterSet.Config as cms

def ESTrivialConditionRetriever(**kwargs):
  mod = cms.ESSource('ESTrivialConditionRetriever',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
