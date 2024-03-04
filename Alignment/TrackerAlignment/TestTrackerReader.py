import FWCore.ParameterSet.Config as cms

def TestTrackerReader(**kwargs):
  mod = cms.EDAnalyzer('TestTrackerReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
