import FWCore.ParameterSet.Config as cms

def MuonBeamspotConstraintValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonBeamspotConstraintValueMapProducer',
    src = cms.InputTag('muons'),
    beamspot = cms.InputTag('offlineBeamSpot'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
