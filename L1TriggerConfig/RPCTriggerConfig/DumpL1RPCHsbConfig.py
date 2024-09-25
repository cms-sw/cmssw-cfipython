import FWCore.ParameterSet.Config as cms

def DumpL1RPCHsbConfig(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpL1RPCHsbConfig',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
