import FWCore.ParameterSet.Config as cms

def dEdxAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('dEdxAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
