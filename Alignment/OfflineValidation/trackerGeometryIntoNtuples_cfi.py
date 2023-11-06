import FWCore.ParameterSet.Config as cms

trackerGeometryIntoNtuples = cms.EDAnalyzer('TrackerGeometryIntoNtuples',
  outputFile = cms.untracked.string(''),
  outputTreename = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
