import FWCore.ParameterSet.Config as cms

def DumpLSTGeometry(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpLSTGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
