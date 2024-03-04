import FWCore.ParameterSet.Config as cms

def TauValCandViewCleaner(**kwargs):
  mod = cms.EDProducer('TauValCandViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
