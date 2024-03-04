import FWCore.ParameterSet.Config as cms

def TestExpressLumiProducer(**kwargs):
  mod = cms.EDAnalyzer('TestExpressLumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
