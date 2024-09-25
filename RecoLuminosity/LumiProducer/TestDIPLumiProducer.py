import FWCore.ParameterSet.Config as cms

def TestDIPLumiProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestDIPLumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
