import FWCore.ParameterSet.Config as cms

phase2TrackerClusterizerValidationTGraph = cms.EDAnalyzer('Phase2TrackerClusterizerValidationTGraph',
  src = cms.string('siPhase2Clusters'),
  links = cms.InputTag('simSiPixelDigis', 'Tracker'),
  mightGet = cms.optional.untracked.vstring
)
