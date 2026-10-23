import FWCore.ParameterSet.Config as cms

def HGCGeomAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCGeomAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
