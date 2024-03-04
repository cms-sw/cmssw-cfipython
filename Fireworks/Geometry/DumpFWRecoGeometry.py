import FWCore.ParameterSet.Config as cms

def DumpFWRecoGeometry(**kwargs):
  mod = cms.EDAnalyzer('DumpFWRecoGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
