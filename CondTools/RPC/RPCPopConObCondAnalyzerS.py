import FWCore.ParameterSet.Config as cms

def RPCPopConObCondAnalyzerS(**kwargs):
  mod = cms.EDAnalyzer('RPCPopConObCondAnalyzerS',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
