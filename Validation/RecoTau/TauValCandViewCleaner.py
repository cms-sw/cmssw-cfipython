import FWCore.ParameterSet.Config as cms

def TauValCandViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('TauValCandViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
