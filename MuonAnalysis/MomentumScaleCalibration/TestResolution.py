import FWCore.ParameterSet.Config as cms

def TestResolution(*args, **kwargs):
  mod = cms.EDAnalyzer('TestResolution',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
