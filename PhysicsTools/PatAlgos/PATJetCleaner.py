import FWCore.ParameterSet.Config as cms

def PATJetCleaner(*args, **kwargs):
  mod = cms.EDProducer('PATJetCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
