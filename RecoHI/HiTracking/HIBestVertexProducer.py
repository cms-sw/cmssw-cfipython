import FWCore.ParameterSet.Config as cms

def HIBestVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('HIBestVertexProducer',
    beamSpotLabel = cms.InputTag('offlineBeamSpot'),
    adaptiveVertexCollection = cms.InputTag('hiBestAdaptiveVertex'),
    medianVertexCollection = cms.InputTag('hiPixelMedianVertex'),
    useFinalAdaptiveVertexCollection = cms.bool(False),
    finalAdaptiveVertexCollection = cms.InputTag('hiBestOfflinePrimaryVertex'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
