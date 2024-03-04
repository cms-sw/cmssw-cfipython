import FWCore.ParameterSet.Config as cms

def RPCPopConObGasAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCPopConObGasAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
