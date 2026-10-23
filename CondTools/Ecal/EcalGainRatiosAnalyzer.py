import FWCore.ParameterSet.Config as cms

def EcalGainRatiosAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalGainRatiosAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
