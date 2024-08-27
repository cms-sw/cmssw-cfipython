import FWCore.ParameterSet.Config as cms

def Phase2TrackerClusterizerValidationTGraph(**kwargs):
  mod = cms.EDAnalyzer('Phase2TrackerClusterizerValidationTGraph',
    src = cms.string('siPhase2Clusters'),
    links = cms.InputTag('simSiPixelDigis', 'Tracker'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
