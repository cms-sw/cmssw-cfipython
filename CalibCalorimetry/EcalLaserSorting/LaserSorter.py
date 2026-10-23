import FWCore.ParameterSet.Config as cms

def LaserSorter(*args, **kwargs):
  mod = cms.EDAnalyzer('LaserSorter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
