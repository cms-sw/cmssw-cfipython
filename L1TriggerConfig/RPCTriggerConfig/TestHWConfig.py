import FWCore.ParameterSet.Config as cms

def TestHWConfig(*args, **kwargs):
  mod = cms.EDAnalyzer('TestHWConfig',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
