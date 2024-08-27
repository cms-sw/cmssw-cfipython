import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGSlidingWindowAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGSlidingWindowAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
