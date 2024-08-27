import FWCore.ParameterSet.Config as cms

def TestLumiProducerFromBrilcalc(**kwargs):
  mod = cms.EDAnalyzer('TestLumiProducerFromBrilcalc',
    inputTag = cms.required.untracked.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
