import FWCore.ParameterSet.Config as cms

def MuonToTrackingParticleAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('MuonToTrackingParticleAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
