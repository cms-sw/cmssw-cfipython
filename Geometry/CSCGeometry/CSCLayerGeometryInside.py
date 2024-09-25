import FWCore.ParameterSet.Config as cms

def CSCLayerGeometryInside(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCLayerGeometryInside',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
