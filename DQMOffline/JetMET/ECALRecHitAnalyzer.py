import FWCore.ParameterSet.Config as cms

def ECALRecHitAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ECALRecHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
