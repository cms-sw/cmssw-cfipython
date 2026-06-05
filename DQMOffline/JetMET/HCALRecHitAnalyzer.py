import FWCore.ParameterSet.Config as cms

def HCALRecHitAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HCALRecHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
