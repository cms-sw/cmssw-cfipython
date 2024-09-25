import FWCore.ParameterSet.Config as cms

def JetTester_HeavyIons(*args, **kwargs):
  mod = cms.EDProducer('JetTester_HeavyIons',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
