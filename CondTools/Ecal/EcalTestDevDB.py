import FWCore.ParameterSet.Config as cms

def EcalTestDevDB(**kwargs):
  mod = cms.EDAnalyzer('EcalTestDevDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
