import FWCore.ParameterSet.Config as cms

def RPCPopConObCondAnalyzerI(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCPopConObCondAnalyzerI',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
