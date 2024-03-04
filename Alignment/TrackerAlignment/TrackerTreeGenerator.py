import FWCore.ParameterSet.Config as cms

def TrackerTreeGenerator(**kwargs):
  mod = cms.EDAnalyzer('TrackerTreeGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
