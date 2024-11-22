import FWCore.ParameterSet.Config as cms

def EcalWeightGroupAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalWeightGroupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
