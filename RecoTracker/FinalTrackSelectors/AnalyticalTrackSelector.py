import FWCore.ParameterSet.Config as cms

def AnalyticalTrackSelector(*args, **kwargs):
  mod = cms.EDProducer('AnalyticalTrackSelector',
    src = cms.InputTag('generalTracks'),
    keepAllTracks = cms.bool(False),
    beamspot = cms.InputTag('offlineBeamSpot'),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag('firstStepPrimaryVertices'),
    vtxNumber = cms.int32(-1),
    vertexCut = cms.string('ndof>=2&!isFake'),
    passThroughForAll = cms.bool(False),
    passThroughForDisplaced = cms.bool(False),
    minLayersForDisplaced = cms.uint32(4),
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    qualityBit = cms.string(''),
    chi2n_no1Dmod_par = cms.double(9999),
    chi2n_par = cms.double(1.6),
    res_par = cms.vdouble(
      0.003,
      0.01
    ),
    d0_par1 = cms.vdouble(
      0.55,
      4
    ),
    d0_par2 = cms.vdouble(
      0.65,
      4
    ),
    dz_par1 = cms.vdouble(
      0.55,
      4
    ),
    dz_par2 = cms.vdouble(
      0.45,
      4
    ),
    applyAdaptedPVCuts = cms.bool(True),
    max_d0 = cms.double(100),
    max_z0 = cms.double(100),
    nSigmaZ = cms.double(4),
    minNumberLayers = cms.uint32(0),
    minNumber3DLayers = cms.uint32(0),
    minHitsToBypassChecks = cms.uint32(20),
    maxNumberLostLayers = cms.uint32(999),
    applyAbsCutsIfNoPV = cms.bool(False),
    max_d0NoPV = cms.double(100),
    max_z0NoPV = cms.double(100),
    max_relpterr = cms.double(9999),
    min_nhits = cms.uint32(0),
    max_lostHitFraction = cms.double(1),
    max_minMissHitOutOrIn = cms.int32(99),
    max_eta = cms.double(9999),
    min_eta = cms.double(-9999),
    useMVA = cms.bool(False),
    useAnyMVA = cms.bool(False),
    useMVAonly = cms.bool(False),
    minMVA = cms.double(-1),
    GBRForestLabel = cms.string('MVASelectorIter0'),
    mvaType = cms.string('Detached'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
