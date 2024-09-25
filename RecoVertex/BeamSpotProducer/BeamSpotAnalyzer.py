import FWCore.ParameterSet.Config as cms

def BeamSpotAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamSpotAnalyzer',
    BSAnalyzerParameters = cms.PSet(
      WriteToDB = cms.bool(False),
      RunAllFitters = cms.bool(False),
      fitEveryNLumi = cms.untracked.int32(-1),
      resetEveryNLumi = cms.untracked.int32(-1),
      RunBeamWidthFit = cms.bool(False)
    ),
    primaryVertex = cms.untracked.InputTag('offlinePrimaryVertices'),
    beamSpot = cms.untracked.InputTag('offlineBeamSpot'),
    BeamFitter = cms.PSet(
      Debug = cms.required.untracked.bool,
      TrackCollection = cms.required.untracked.InputTag,
      WriteAscii = cms.required.untracked.bool,
      AsciiFileName = cms.required.untracked.string,
      AppendRunToFileName = cms.required.untracked.bool,
      WriteDIPAscii = cms.required.untracked.bool,
      WriteDIPOnBadFit = cms.untracked.bool(True),
      DIPFileName = cms.required.untracked.string,
      SaveNtuple = cms.required.untracked.bool,
      SaveFitResults = cms.required.untracked.bool,
      SavePVVertices = cms.required.untracked.bool,
      IsMuonCollection = cms.required.untracked.bool,
      MinimumPt = cms.required.untracked.double,
      MaximumEta = cms.required.untracked.double,
      MaximumImpactParameter = cms.required.untracked.double,
      MaximumZ = cms.required.untracked.double,
      MinimumTotalLayers = cms.required.untracked.int32,
      MinimumPixelLayers = cms.required.untracked.int32,
      MaximumNormChi2 = cms.required.untracked.double,
      TrackAlgorithm = cms.required.untracked.vstring,
      TrackQuality = cms.required.untracked.vstring,
      MinimumInputTracks = cms.required.untracked.int32,
      FractionOfFittedTrks = cms.required.untracked.double,
      InputBeamWidth = cms.untracked.double(-1),
      OutputFileName = cms.untracked.string('')
    ),
    PVFitter = cms.PSet(
      Debug = cms.required.untracked.bool,
      VertexCollection = cms.untracked.InputTag('offlinePrimaryVertices'),
      Apply3DFit = cms.required.untracked.bool,
      maxNrStoredVertices = cms.required.untracked.uint32,
      minNrVerticesForFit = cms.required.untracked.uint32,
      minVertexNdf = cms.required.untracked.double,
      maxVertexNormChi2 = cms.required.untracked.double,
      minVertexNTracks = cms.required.untracked.uint32,
      minVertexMeanWeight = cms.required.untracked.double,
      maxVertexR = cms.required.untracked.double,
      maxVertexZ = cms.required.untracked.double,
      errorScale = cms.required.untracked.double,
      nSigmaCut = cms.required.untracked.double,
      FitPerBunchCrossing = cms.required.untracked.bool,
      useOnlyFirstPV = cms.required.untracked.bool,
      minSumPt = cms.required.untracked.double
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
