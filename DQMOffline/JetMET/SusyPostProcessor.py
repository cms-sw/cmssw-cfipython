import FWCore.ParameterSet.Config as cms

def SusyPostProcessor(*args, **kwargs):
  mod = cms.EDProducer('SusyPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
