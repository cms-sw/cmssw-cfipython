import FWCore.ParameterSet.Config as cms

def TestMTDIdealGeometry(**kwargs):
  mod = cms.EDAnalyzer('TestMTDIdealGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
