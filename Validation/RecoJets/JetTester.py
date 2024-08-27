import FWCore.ParameterSet.Config as cms

def JetTester(**kwargs):
  mod = cms.EDProducer('JetTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
