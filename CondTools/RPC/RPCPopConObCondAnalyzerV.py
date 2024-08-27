import FWCore.ParameterSet.Config as cms

def RPCPopConObCondAnalyzerV(**kwargs):
  mod = cms.EDAnalyzer('RPCPopConObCondAnalyzerV',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
