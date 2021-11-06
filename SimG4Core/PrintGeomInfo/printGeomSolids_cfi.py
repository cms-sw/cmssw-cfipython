import FWCore.ParameterSet.Config as cms

printGeomSolids = cms.EDAnalyzer('PrintGeomSolids',
  fromDD4hep = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
