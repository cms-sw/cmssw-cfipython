import FWCore.ParameterSet.Config as cms

def EcalTrigPrimAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalTrigPrimAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
