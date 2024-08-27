import FWCore.ParameterSet.Config as cms

def BoostedTauSeedsProducer(**kwargs):
  mod = cms.EDProducer('BoostedTauSeedsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
