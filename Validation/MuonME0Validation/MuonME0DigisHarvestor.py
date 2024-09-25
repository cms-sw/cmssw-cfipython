import FWCore.ParameterSet.Config as cms

def MuonME0DigisHarvestor(*args, **kwargs):
  mod = cms.EDProducer('MuonME0DigisHarvestor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
