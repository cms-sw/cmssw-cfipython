import FWCore.ParameterSet.Config as cms

def DDTestDumpGeometry(*args, **kwargs):
  mod = cms.EDAnalyzer('DDTestDumpGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
