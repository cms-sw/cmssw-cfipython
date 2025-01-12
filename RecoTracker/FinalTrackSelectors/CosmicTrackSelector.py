import FWCore.ParameterSet.Config as cms

def CosmicTrackSelector(*args, **kwargs):
  mod = cms.EDProducer('CosmicTrackSelector',
    src = cms.InputTag('ctfWithMaterialTracksCosmics'),
    beamspot = cms.InputTag('offlineBeamSpot'),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    keepAllTracks = cms.bool(False),
    chi2n_par = cms.double(10),
    max_d0 = cms.double(110),
    max_z0 = cms.double(300),
    min_pt = cms.double(1),
    max_eta = cms.double(2),
    min_nHit = cms.uint32(5),
    min_nPixelHit = cms.uint32(0),
    minNumberLayers = cms.uint32(0),
    minNumber3DLayers = cms.uint32(0),
    maxNumberLostLayers = cms.uint32(999),
    qualityBit = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
