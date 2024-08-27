import FWCore.ParameterSet.Config as cms

def EcalShowerContainmentAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalShowerContainmentAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
