import FWCore.ParameterSet.Config as cms

def EcalTrivialObjectAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalTrivialObjectAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
