import FWCore.ParameterSet.Config as cms

hgcalPartialCellTester = cms.EDAnalyzer('HGCalPartialCellTester',
  waferSize = cms.double(166.4408),
  waferType = cms.int32(1),
  cellPlacementIndex = cms.int32(2),
  partialType = cms.int32(11),
  numbberOfTrials = cms.int32(1000),
  modeUV = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
