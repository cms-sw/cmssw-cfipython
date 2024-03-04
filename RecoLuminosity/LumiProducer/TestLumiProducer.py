import FWCore.ParameterSet.Config as cms

def TestLumiProducer(**kwargs):
  mod = cms.EDAnalyzer('TestLumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
