import FWCore.ParameterSet.Config as cms

def EventTimeDistribution(**kwargs):
  mod = cms.EDAnalyzer('EventTimeDistribution',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
