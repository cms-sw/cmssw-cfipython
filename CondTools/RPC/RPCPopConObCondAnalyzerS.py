import FWCore.ParameterSet.Config as cms

def RPCPopConObCondAnalyzerS(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCPopConObCondAnalyzerS',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
