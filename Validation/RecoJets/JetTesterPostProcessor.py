import FWCore.ParameterSet.Config as cms

def JetTesterPostProcessor(*args, **kwargs):
  mod = cms.EDProducer('JetTesterPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
