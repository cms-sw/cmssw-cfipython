import FWCore.ParameterSet.Config as cms

def PrintGeomSolids(*args, **kwargs):
  mod = cms.EDAnalyzer('PrintGeomSolids',
    fromDD4hep = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
