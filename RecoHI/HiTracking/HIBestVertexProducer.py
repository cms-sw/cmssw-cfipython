import FWCore.ParameterSet.Config as cms

def HIBestVertexProducer(**kwargs):
  mod = cms.EDProducer('HIBestVertexProducer',
    beamSpotLabel = cms.InputTag('offlineBeamSpot'),
    adaptiveVertexCollection = cms.InputTag('hiBestAdaptiveVertex'),
    medianVertexCollection = cms.InputTag('hiPixelMedianVertex'),
    useFinalAdaptiveVertexCollection = cms.bool(False),
    finalAdaptiveVertexCollection = cms.InputTag('hiBestOfflinePrimaryVertex'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
