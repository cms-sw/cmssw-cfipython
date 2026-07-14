import FWCore.ParameterSet.Config as cms

def BranchTrackerReplacementValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('BranchTrackerReplacementValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
