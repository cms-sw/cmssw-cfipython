import FWCore.ParameterSet.Config as cms

def PrintGeomSolids(**kwargs):
  mod = cms.EDAnalyzer('PrintGeomSolids',
    fromDD4hep = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
