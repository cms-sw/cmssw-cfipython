import FWCore.ParameterSet.Config as cms

def RPCPopConObCondAnalyzerI(**kwargs):
  mod = cms.EDAnalyzer('RPCPopConObCondAnalyzerI',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
