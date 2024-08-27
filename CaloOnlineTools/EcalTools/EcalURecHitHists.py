import FWCore.ParameterSet.Config as cms

def EcalURecHitHists(**kwargs):
  mod = cms.EDAnalyzer('EcalURecHitHists',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
