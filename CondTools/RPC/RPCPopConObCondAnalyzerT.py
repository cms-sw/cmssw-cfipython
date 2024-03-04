import FWCore.ParameterSet.Config as cms

def RPCPopConObCondAnalyzerT(**kwargs):
  mod = cms.EDAnalyzer('RPCPopConObCondAnalyzerT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
