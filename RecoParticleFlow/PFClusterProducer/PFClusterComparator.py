import FWCore.ParameterSet.Config as cms

def PFClusterComparator(*args, **kwargs):
  mod = cms.EDAnalyzer('PFClusterComparator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
