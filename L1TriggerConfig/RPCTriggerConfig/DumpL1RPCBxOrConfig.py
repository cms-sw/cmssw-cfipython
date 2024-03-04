import FWCore.ParameterSet.Config as cms

def DumpL1RPCBxOrConfig(**kwargs):
  mod = cms.EDAnalyzer('DumpL1RPCBxOrConfig',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
