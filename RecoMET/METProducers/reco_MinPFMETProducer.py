import FWCore.ParameterSet.Config as cms

def reco_MinPFMETProducer(*args, **kwargs):
  mod = cms.EDProducer('reco::MinPFMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
