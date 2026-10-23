import FWCore.ParameterSet.Config as cms

def DumpFWRecoGeometry(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpFWRecoGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
