import FWCore.ParameterSet.Config as cms

def L1TkHTMissProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TkHTMissProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
