import FWCore.ParameterSet.Config as cms

def CSCGeometryAsLayers(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGeometryAsLayers',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
