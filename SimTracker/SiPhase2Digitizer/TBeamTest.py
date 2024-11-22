import FWCore.ParameterSet.Config as cms

def TBeamTest(*args, **kwargs):
  mod = cms.EDProducer('TBeamTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
