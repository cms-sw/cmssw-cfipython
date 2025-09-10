import FWCore.ParameterSet.Config as cms

def TestAccessGeom(*args, **kwargs):
  mod = cms.EDAnalyzer('TestAccessGeom',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
