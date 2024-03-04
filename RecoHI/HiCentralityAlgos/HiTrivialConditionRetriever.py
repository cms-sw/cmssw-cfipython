import FWCore.ParameterSet.Config as cms

def HiTrivialConditionRetriever(**kwargs):
  mod = cms.ESSource('HiTrivialConditionRetriever',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
