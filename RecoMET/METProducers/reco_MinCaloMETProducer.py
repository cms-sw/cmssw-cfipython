import FWCore.ParameterSet.Config as cms

def reco_MinCaloMETProducer(*args, **kwargs):
  mod = cms.EDProducer('reco::MinCaloMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
