import FWCore.ParameterSet.Config as cms

def GeneralPurposeVertexAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GeneralPurposeVertexAnalyzer',
    ndof = cms.int32(4),
    vertexLabel = cms.InputTag('offlinePrimaryVertices'),
    beamSpotLabel = cms.InputTag('offlineBeamSpot'),
    Xpos = cms.double(0.1),
    Ypos = cms.double(0),
    TkSizeBin = cms.int32(100),
    TkSizeMin = cms.double(499.5),
    TkSizeMax = cms.double(-0.5),
    DxyBin = cms.int32(100),
    DxyMin = cms.double(5000),
    DxyMax = cms.double(-5000),
    DzBin = cms.int32(100),
    DzMin = cms.double(-2000),
    DzMax = cms.double(2000),
    PhiBin = cms.int32(32),
    PhiBin2D = cms.int32(12),
    PhiMin = cms.double(-3.1415926535897931),
    PhiMax = cms.double(3.1415926535897931),
    EtaBin = cms.int32(26),
    EtaBin2D = cms.int32(8),
    EtaMin = cms.double(-2.7),
    EtaMax = cms.double(2.7),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
