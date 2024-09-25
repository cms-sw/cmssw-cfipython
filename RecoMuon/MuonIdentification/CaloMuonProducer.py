import FWCore.ParameterSet.Config as cms

def CaloMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('CaloMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
