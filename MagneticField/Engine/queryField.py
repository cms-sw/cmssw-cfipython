import FWCore.ParameterSet.Config as cms

def queryField(**kwargs):
  mod = cms.EDAnalyzer('queryField',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
