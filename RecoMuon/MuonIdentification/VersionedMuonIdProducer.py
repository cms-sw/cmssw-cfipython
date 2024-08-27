import FWCore.ParameterSet.Config as cms

def VersionedMuonIdProducer(**kwargs):
  mod = cms.EDProducer('VersionedMuonIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
