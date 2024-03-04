import FWCore.ParameterSet.Config as cms

def DumpL1RPCHsbConfig(**kwargs):
  mod = cms.EDAnalyzer('DumpL1RPCHsbConfig',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
