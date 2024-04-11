import FWCore.ParameterSet.Config as cms

hgcalCellOffsetTester = cms.EDAnalyzer('HGCalCellOffsetTester',
  waferSize = cms.double(167.4408),
  waferType = cms.int32(0),
  cellPlacementIndex = cms.int32(11),
  cellType = cms.int32(22),
  mouseBiteCut = cms.double(5),
  guardRingOffset = cms.double(0.9),
  mightGet = cms.optional.untracked.vstring
)
