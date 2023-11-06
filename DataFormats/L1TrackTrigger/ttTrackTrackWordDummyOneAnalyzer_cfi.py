import FWCore.ParameterSet.Config as cms

ttTrackTrackWordDummyOneAnalyzer = cms.EDAnalyzer('TTTrackTrackWordDummyOneAnalyzer',
  mightGet = cms.optional.untracked.vstring
)
