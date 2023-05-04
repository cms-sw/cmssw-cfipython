import FWCore.ParameterSet.Config as cms

me0GeometryDump = cms.EDAnalyzer('ME0GeometryDump',
  verbose = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
