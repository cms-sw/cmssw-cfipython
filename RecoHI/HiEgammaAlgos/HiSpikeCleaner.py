import FWCore.ParameterSet.Config as cms

def HiSpikeCleaner(*args, **kwargs):
  mod = cms.EDProducer('HiSpikeCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
