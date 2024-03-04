import FWCore.ParameterSet.Config as cms

def TrackerMapTool(**kwargs):
  mod = cms.EDAnalyzer('TrackerMapTool',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
