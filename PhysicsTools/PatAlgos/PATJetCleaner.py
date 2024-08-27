import FWCore.ParameterSet.Config as cms

def PATJetCleaner(**kwargs):
  mod = cms.EDProducer('PATJetCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
