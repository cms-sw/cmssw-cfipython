import FWCore.ParameterSet.Config as cms

def PixelVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelVertexProducer',
    Verbosity = cms.int32(0),
    PtMin = cms.double(1),
    Method2 = cms.bool(True),
    TrackCollection = cms.InputTag('pixelTracks'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    Finder = cms.string('DivisiveVertexFinder'),
    UseError = cms.bool(True),
    WtAverage = cms.bool(True),
    ZOffset = cms.double(5),
    ZSeparation = cms.double(0.05),
    NTrkMin = cms.int32(2),
    PVcomparer = cms.PSet(
      track_pt_min = cms.double(1),
      track_pt_max = cms.double(10),
      track_chi2_max = cms.double(999999),
      track_prob_min = cms.double(-1)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
