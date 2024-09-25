import FWCore.ParameterSet.Config as cms

def TrackerDpgAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackerDpgAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
