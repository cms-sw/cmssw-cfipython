import FWCore.ParameterSet.Config as cms

def ESTrivialConditionRetriever(*args, **kwargs):
  mod = cms.ESSource('ESTrivialConditionRetriever',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
