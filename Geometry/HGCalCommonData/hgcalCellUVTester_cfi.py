import FWCore.ParameterSet.Config as cms

hgcalCellUVTester = cms.EDAnalyzer('HGCalCellUVTester',
  waferSize = cms.double(166.4408),
  waferType = cms.int32(1),
  cellPlacementIndex = cms.int32(6),
  mightGet = cms.optional.untracked.vstring
)
