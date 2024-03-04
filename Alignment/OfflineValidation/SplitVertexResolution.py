import FWCore.ParameterSet.Config as cms

def SplitVertexResolution(**kwargs):
  mod = cms.EDAnalyzer('SplitVertexResolution',
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
    nTrackBins = cms.untracked.double(120),
    nVtxBins = cms.untracked.double(60),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
