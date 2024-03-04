import FWCore.ParameterSet.Config as cms

def DumpL1RPCConfig(**kwargs):
  mod = cms.EDAnalyzer('DumpL1RPCConfig',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
