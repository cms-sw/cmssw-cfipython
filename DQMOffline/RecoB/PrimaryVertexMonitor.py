import FWCore.ParameterSet.Config as cms

def PrimaryVertexMonitor(*args, **kwargs):
  mod = cms.EDProducer('PrimaryVertexMonitor',
    TopFolderName = cms.string('OfflinePV'),
    AlignmentLabel = cms.string('Alignment'),
    ndof = cms.int32(4),
    useHPforAlignmentPlots = cms.bool(True),
    vertexLabel = cms.InputTag('offlinePrimaryVertices'),
    beamSpotLabel = cms.InputTag('offlineBeamSpot'),
    PUMax = cms.double(80),
    Xpos = cms.double(0.1),
    Ypos = cms.double(0),
    TkSizeBin = cms.int32(100),
    TkSizeMin = cms.double(-0.5),
    TkSizeMax = cms.double(499.5),
    DxyBin = cms.int32(100),
    DxyMin = cms.double(-5000),
    DxyMax = cms.double(5000),
    DzBin = cms.int32(100),
    DzMin = cms.double(-2000),
    DzMax = cms.double(2000),
    PhiBin = cms.int32(32),
    PhiMin = cms.double(-3.1415926535897931),
    PhiMax = cms.double(3.1415926535897931),
    EtaBin = cms.int32(26),
    EtaMin = cms.double(2.5),
    EtaMax = cms.double(-2.5),
    PhiBin2D = cms.int32(12),
    EtaBin2D = cms.int32(8),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
