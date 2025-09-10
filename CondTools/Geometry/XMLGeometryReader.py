import FWCore.ParameterSet.Config as cms

def XMLGeometryReader(*args, **kwargs):
  mod = cms.EDAnalyzer('XMLGeometryReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
