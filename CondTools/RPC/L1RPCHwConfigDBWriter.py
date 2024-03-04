import FWCore.ParameterSet.Config as cms

def L1RPCHwConfigDBWriter(**kwargs):
  mod = cms.EDAnalyzer('L1RPCHwConfigDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
