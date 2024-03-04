import FWCore.ParameterSet.Config as cms

def TestIdealGeometry2(**kwargs):
  mod = cms.EDAnalyzer('TestIdealGeometry2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
