import FWCore.ParameterSet.Config as cms

def DumpL1RPCConfig(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpL1RPCConfig',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
