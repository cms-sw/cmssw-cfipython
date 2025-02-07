import FWCore.ParameterSet.Config as cms

def RPCRecoIdealDBLoader(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCRecoIdealDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
