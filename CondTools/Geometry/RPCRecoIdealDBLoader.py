import FWCore.ParameterSet.Config as cms

def RPCRecoIdealDBLoader(**kwargs):
  mod = cms.EDAnalyzer('RPCRecoIdealDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
