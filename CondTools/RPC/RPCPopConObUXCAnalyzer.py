import FWCore.ParameterSet.Config as cms

def RPCPopConObUXCAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCPopConObUXCAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
