import FWCore.ParameterSet.Config as cms

testglobalrunsummary = cms.EDProducer('testTkHistoMap',
  readFromFile = cms.bool(False),
  inputFile = cms.FileInPath('CalibTracker/SiStripCommon/data/SiStripDetInfo.dat'),
  mightGet = cms.optional.untracked.vstring
)
