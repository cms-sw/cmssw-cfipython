import FWCore.ParameterSet.Config as cms

def HiPartonCleaner(*args, **kwargs):
  mod = cms.EDProducer('HiPartonCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
