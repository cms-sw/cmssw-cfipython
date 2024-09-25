import FWCore.ParameterSet.Config as cms

def Phase2TrackerClusterizerValidationTGraph(*args, **kwargs):
  mod = cms.EDAnalyzer('Phase2TrackerClusterizerValidationTGraph',
    src = cms.string('siPhase2Clusters'),
    links = cms.InputTag('simSiPixelDigis', 'Tracker'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
