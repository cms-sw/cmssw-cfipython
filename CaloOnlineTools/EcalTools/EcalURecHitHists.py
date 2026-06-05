import FWCore.ParameterSet.Config as cms

def EcalURecHitHists(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalURecHitHists',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
