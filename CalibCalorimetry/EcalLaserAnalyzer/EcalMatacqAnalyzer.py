import FWCore.ParameterSet.Config as cms

def EcalMatacqAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalMatacqAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
