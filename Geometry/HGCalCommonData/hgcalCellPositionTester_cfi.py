import FWCore.ParameterSet.Config as cms

hgcalCellPositionTester = cms.EDAnalyzer('HGCalCellPositionTester',
  waferSize = cms.double(166.4408),
  waferType = cms.int32(0),
  cellPlacementIndex = cms.int32(7),
  mightGet = cms.optional.untracked.vstring
)
