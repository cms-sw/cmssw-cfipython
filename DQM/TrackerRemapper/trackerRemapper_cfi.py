import FWCore.ParameterSet.Config as cms

trackerRemapper = cms.EDAnalyzer('TrackerRemapper',
  src = cms.InputTag('generalTracks'),
  opMode = cms.int32(0),
  analyzeMode = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)
