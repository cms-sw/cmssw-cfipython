import FWCore.ParameterSet.Config as cms

def Phase2TrackerClusterizerValidation(**kwargs):
  mod = cms.EDAnalyzer('Phase2TrackerClusterizerValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
