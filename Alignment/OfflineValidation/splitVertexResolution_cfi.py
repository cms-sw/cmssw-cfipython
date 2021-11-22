import FWCore.ParameterSet.Config as cms

splitVertexResolution = cms.EDAnalyzer('SplitVertexResolution',
  compressionSettings = cms.untracked.int32(-1),
  storeNtuple = cms.bool(False),
  intLumi = cms.untracked.double(0),
  Debug = cms.untracked.bool(False),
  vtxCollection = cms.InputTag('offlinePrimaryVertices'),
  trackCollection = cms.InputTag('generalTracks'),
  minVertexNdf = cms.untracked.double(10),
  minVertexMeanWeight = cms.untracked.double(0.5),
  runControl = cms.untracked.bool(False),
  runControlNumber = cms.untracked.vuint32(),
  sumpTStartScale = cms.untracked.double(1),
  sumpTEndScale = cms.untracked.double(1000),
  nTrackBins = cms.untracked.double(60),
  nVtxBins = cms.untracked.double(40),
  mightGet = cms.optional.untracked.vstring
)