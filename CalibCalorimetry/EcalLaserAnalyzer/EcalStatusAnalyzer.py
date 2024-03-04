import FWCore.ParameterSet.Config as cms

def EcalStatusAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalStatusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
