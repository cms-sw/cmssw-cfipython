import FWCore.ParameterSet.Config as cms

def EcalTPCondAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalTPCondAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
