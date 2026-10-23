import FWCore.ParameterSet.Config as cms

def EcalShowerContainmentAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalShowerContainmentAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
