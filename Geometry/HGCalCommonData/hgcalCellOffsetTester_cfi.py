import FWCore.ParameterSet.Config as cms

hgcalCellOffsetTester = cms.EDAnalyzer('HGCalCellOffsetTester',
  waferSize = cms.double(166.4408),
  waferType = cms.int32(0),
  cellPlacementIndex = cms.int32(3),
  mouseBiteCut = cms.double(0),
  guardRingOffset = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
