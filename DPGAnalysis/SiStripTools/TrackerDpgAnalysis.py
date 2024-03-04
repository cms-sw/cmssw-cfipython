import FWCore.ParameterSet.Config as cms

def TrackerDpgAnalysis(**kwargs):
  mod = cms.EDAnalyzer('TrackerDpgAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
