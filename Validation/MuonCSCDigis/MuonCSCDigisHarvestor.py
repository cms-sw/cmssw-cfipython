import FWCore.ParameterSet.Config as cms

def MuonCSCDigisHarvestor(*args, **kwargs):
  mod = cms.EDProducer('MuonCSCDigisHarvestor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
