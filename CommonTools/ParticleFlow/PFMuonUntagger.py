import FWCore.ParameterSet.Config as cms

def PFMuonUntagger(*args, **kwargs):
  mod = cms.EDProducer('PFMuonUntagger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
