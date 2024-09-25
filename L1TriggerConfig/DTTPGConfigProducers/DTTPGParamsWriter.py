import FWCore.ParameterSet.Config as cms

def DTTPGParamsWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTPGParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
