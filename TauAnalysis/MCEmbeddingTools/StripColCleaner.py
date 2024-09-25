import FWCore.ParameterSet.Config as cms

def StripColCleaner(*args, **kwargs):
  mod = cms.EDProducer('StripColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
