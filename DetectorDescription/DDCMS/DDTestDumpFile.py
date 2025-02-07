import FWCore.ParameterSet.Config as cms

def DDTestDumpFile(*args, **kwargs):
  mod = cms.EDAnalyzer('DDTestDumpFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
