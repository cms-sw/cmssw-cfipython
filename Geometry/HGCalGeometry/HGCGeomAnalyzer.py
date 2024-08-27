import FWCore.ParameterSet.Config as cms

def HGCGeomAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HGCGeomAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
