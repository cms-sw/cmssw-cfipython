import FWCore.ParameterSet.Config as cms

def MuonBeamspotConstraintValueMapProducer(**kwargs):
  mod = cms.EDProducer('MuonBeamspotConstraintValueMapProducer',
    src = cms.InputTag('muons'),
    beamspot = cms.InputTag('offlineBeamSpot'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
