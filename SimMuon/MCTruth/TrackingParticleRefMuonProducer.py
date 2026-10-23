import FWCore.ParameterSet.Config as cms

def TrackingParticleRefMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackingParticleRefMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
