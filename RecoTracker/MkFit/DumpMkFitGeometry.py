import FWCore.ParameterSet.Config as cms

def DumpMkFitGeometry(**kwargs):
  mod = cms.EDAnalyzer('DumpMkFitGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
