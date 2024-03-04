import FWCore.ParameterSet.Config as cms

def DumpFWTGeoRecoGeometry(**kwargs):
  mod = cms.EDAnalyzer('DumpFWTGeoRecoGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
