import FWCore.ParameterSet.Config as cms

def ClusterBigEventsDebugger(*args, **kwargs):
  mod = cms.EDAnalyzer('ClusterBigEventsDebugger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
