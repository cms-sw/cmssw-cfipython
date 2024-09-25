import FWCore.ParameterSet.Config as cms

def TestLumiProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestLumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
