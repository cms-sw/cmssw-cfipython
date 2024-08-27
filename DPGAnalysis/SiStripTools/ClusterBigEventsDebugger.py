import FWCore.ParameterSet.Config as cms

def ClusterBigEventsDebugger(**kwargs):
  mod = cms.EDAnalyzer('ClusterBigEventsDebugger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
