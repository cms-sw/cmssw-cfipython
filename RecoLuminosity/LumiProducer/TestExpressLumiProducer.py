import FWCore.ParameterSet.Config as cms

def TestExpressLumiProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestExpressLumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
