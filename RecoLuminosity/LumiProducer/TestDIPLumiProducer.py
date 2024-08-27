import FWCore.ParameterSet.Config as cms

def TestDIPLumiProducer(**kwargs):
  mod = cms.EDAnalyzer('TestDIPLumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
