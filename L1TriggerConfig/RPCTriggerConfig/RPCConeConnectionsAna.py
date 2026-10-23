import FWCore.ParameterSet.Config as cms

def RPCConeConnectionsAna(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCConeConnectionsAna',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
