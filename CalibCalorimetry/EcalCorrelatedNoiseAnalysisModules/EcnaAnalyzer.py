import FWCore.ParameterSet.Config as cms

def EcnaAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcnaAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
