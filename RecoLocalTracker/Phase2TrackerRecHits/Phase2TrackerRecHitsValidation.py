import FWCore.ParameterSet.Config as cms

def Phase2TrackerRecHitsValidation(**kwargs):
  mod = cms.EDAnalyzer('Phase2TrackerRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
