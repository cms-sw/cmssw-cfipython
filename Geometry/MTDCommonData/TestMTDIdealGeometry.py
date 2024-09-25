import FWCore.ParameterSet.Config as cms

def TestMTDIdealGeometry(*args, **kwargs):
  mod = cms.EDAnalyzer('TestMTDIdealGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
