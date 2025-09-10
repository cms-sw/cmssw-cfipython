import FWCore.ParameterSet.Config as cms

def METTesterPostProcessor(*args, **kwargs):
  mod = cms.EDProducer('METTesterPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
