import FWCore.ParameterSet.Config as cms

def HTo2XTo4LGunProducer(*args, **kwargs):
  mod = cms.EDProducer('HTo2XTo4LGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
