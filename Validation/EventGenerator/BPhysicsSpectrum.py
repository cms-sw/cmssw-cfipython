import FWCore.ParameterSet.Config as cms

def BPhysicsSpectrum(*args, **kwargs):
  mod = cms.EDProducer('BPhysicsSpectrum',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
