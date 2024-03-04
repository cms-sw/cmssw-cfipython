import FWCore.ParameterSet.Config as cms

def CSCGeometryAsLayers(**kwargs):
  mod = cms.EDAnalyzer('CSCGeometryAsLayers',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
