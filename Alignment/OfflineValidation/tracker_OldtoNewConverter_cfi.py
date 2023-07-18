import FWCore.ParameterSet.Config as cms

tracker_OldtoNewConverter = cms.EDAnalyzer('Tracker_OldtoNewConverter',
  conversionType = cms.untracked.string(''),
  inputFile = cms.untracked.string(''),
  outputFile = cms.untracked.string(''),
  textFile = cms.untracked.string(''),
  treeName = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
