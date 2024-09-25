import FWCore.ParameterSet.Config as cms

def MuonME0SegHarvestor(*args, **kwargs):
  mod = cms.EDProducer('MuonME0SegHarvestor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
