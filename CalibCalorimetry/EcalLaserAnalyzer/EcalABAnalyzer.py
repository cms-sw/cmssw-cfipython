import FWCore.ParameterSet.Config as cms

def EcalABAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalABAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
