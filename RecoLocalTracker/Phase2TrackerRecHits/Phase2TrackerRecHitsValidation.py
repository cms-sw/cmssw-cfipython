import FWCore.ParameterSet.Config as cms

def Phase2TrackerRecHitsValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('Phase2TrackerRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
