import FWCore.ParameterSet.Config as cms

def CSCLayerGeometryInside(**kwargs):
  mod = cms.EDAnalyzer('CSCLayerGeometryInside',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
