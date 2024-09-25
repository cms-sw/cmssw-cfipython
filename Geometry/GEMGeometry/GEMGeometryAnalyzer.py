import FWCore.ParameterSet.Config as cms

def GEMGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GEMGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
