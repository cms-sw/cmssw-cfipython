import FWCore.ParameterSet.Config as cms

def TestLumiCorrectionSource(**kwargs):
  mod = cms.EDAnalyzer('TestLumiCorrectionSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
