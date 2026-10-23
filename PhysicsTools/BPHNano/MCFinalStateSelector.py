import FWCore.ParameterSet.Config as cms

def MCFinalStateSelector(*args, **kwargs):
  mod = cms.EDProducer('MCFinalStateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
