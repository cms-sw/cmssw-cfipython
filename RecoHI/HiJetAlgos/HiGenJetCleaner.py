import FWCore.ParameterSet.Config as cms

def HiGenJetCleaner(**kwargs):
  mod = cms.EDProducer('HiGenJetCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
