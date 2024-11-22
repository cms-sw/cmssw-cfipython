import FWCore.ParameterSet.Config as cms

def JetTester(*args, **kwargs):
  mod = cms.EDProducer('JetTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
