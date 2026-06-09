import FWCore.ParameterSet.Config as cms

def RPCPopConObCondAnalyzerV(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCPopConObCondAnalyzerV',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
