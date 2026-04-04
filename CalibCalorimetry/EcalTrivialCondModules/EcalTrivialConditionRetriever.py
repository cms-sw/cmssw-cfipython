import FWCore.ParameterSet.Config as cms

def EcalTrivialConditionRetriever(*args, **kwargs):
  mod = cms.ESSource('EcalTrivialConditionRetriever',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
