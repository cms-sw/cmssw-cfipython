import FWCore.ParameterSet.Config as cms

cscGeometryDump = cms.EDAnalyzer('CSCGeometryDump',
  verbose = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
