import FWCore.ParameterSet.Config as cms

def RPCDigiReader(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCDigiReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
