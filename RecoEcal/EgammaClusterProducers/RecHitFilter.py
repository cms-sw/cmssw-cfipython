import FWCore.ParameterSet.Config as cms

def RecHitFilter(*args, **kwargs):
  mod = cms.EDProducer('RecHitFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod