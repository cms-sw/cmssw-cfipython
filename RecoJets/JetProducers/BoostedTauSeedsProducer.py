import FWCore.ParameterSet.Config as cms

def BoostedTauSeedsProducer(*args, **kwargs):
  mod = cms.EDProducer('BoostedTauSeedsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
