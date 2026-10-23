import FWCore.ParameterSet.Config as cms

def MuonGEMRecHitsHarvestor(*args, **kwargs):
  mod = cms.EDProducer('MuonGEMRecHitsHarvestor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
