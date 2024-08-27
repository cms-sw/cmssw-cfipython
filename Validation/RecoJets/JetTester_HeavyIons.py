import FWCore.ParameterSet.Config as cms

def JetTester_HeavyIons(**kwargs):
  mod = cms.EDProducer('JetTester_HeavyIons',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
