import FWCore.ParameterSet.Config as cms

hgcGeometryTester = cms.EDAnalyzer('HGCGeometryTester',
  SquareType = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
