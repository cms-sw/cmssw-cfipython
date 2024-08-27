import FWCore.ParameterSet.Config as cms

def TrackingParticleRefMuonProducer(**kwargs):
  mod = cms.EDProducer('TrackingParticleRefMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
