import FWCore.ParameterSet.Config as cms

def MuonSelectionTypeValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonSelectionTypeValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
