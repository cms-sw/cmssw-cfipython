import FWCore.ParameterSet.Config as cms

def DumpMkFitGeometry(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpMkFitGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
