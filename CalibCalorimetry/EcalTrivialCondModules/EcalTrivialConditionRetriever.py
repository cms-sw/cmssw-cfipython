import FWCore.ParameterSet.Config as cms

def EcalTrivialConditionRetriever(**kwargs):
  mod = cms.ESSource('EcalTrivialConditionRetriever',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
