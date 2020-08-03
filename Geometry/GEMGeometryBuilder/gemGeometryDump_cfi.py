import FWCore.ParameterSet.Config as cms

gemGeometryDump = cms.EDAnalyzer('GEMGeometryDump',
  verbose = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
