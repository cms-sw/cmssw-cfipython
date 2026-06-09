import FWCore.ParameterSet.Config as cms

def TestIdealGeometry2(*args, **kwargs):
  mod = cms.EDAnalyzer('TestIdealGeometry2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
