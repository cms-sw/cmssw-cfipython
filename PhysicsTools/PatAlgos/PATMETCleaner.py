import FWCore.ParameterSet.Config as cms

def PATMETCleaner(*args, **kwargs):
  mod = cms.EDProducer('PATMETCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
