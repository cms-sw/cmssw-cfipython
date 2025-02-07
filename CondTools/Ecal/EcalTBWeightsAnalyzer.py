import FWCore.ParameterSet.Config as cms

def EcalTBWeightsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTBWeightsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
