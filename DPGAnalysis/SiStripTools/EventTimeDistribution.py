import FWCore.ParameterSet.Config as cms

def EventTimeDistribution(*args, **kwargs):
  mod = cms.EDAnalyzer('EventTimeDistribution',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
