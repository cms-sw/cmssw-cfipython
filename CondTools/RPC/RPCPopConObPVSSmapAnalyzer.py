import FWCore.ParameterSet.Config as cms

def RPCPopConObPVSSmapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCPopConObPVSSmapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
