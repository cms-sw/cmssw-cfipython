import FWCore.ParameterSet.Config as cms

def MuonToTrackingParticleAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonToTrackingParticleAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
