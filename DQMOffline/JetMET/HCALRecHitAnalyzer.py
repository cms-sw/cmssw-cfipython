import FWCore.ParameterSet.Config as cms

def HCALRecHitAnalyzer(**kwargs):
  mod = cms.EDProducer('HCALRecHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
