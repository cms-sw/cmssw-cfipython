import FWCore.ParameterSet.Config as cms

def DumpFWTGeoRecoGeometry(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpFWTGeoRecoGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
