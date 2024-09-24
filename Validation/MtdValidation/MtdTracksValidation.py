import FWCore.ParameterSet.Config as cms

def MtdTracksValidation(**kwargs):
  mod = cms.EDProducer('MtdTracksValidation',
    folder = cms.string('MTD/Tracks'),
    inputTagG = cms.InputTag('generalTracks'),
    inputTagT = cms.InputTag('trackExtenderWithMTD'),
    inputTagV = cms.InputTag('offlinePrimaryVertices4D'),
    inputTagH = cms.InputTag('generatorSmeared'),
    SimTag = cms.InputTag('mix', 'MergedTrackTruth'),
    TPtoRecoTrackAssoc = cms.InputTag('trackingParticleRecoTrackAsssociation'),
    tp2SimAssociationMapTag = cms.InputTag('mtdSimLayerClusterToTPAssociation'),
    btlRecHits = cms.InputTag('mtdRecHits', 'FTLBarrel'),
    etlRecHits = cms.InputTag('mtdRecHits', 'FTLEndcap'),
    tmtd = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
    sigmatmtd = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmatmtd'),
    t0Src = cms.InputTag('trackExtenderWithMTD', 'generalTrackt0'),
    sigmat0Src = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmat0'),
    trackAssocSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackassoc'),
    pathLengthSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackPathLength'),
    t0SafePID = cms.InputTag('tofPID', 't0safe'),
    sigmat0SafePID = cms.InputTag('tofPID', 'sigmat0safe'),
    sigmat0PID = cms.InputTag('tofPID', 'sigmat0'),
    t0PID = cms.InputTag('tofPID', 't0'),
    sigmaTofPi = cms.InputTag('trackExtenderWithMTD', 'generalTrackSigmaTofPi'),
    sigmaTofK = cms.InputTag('trackExtenderWithMTD', 'generalTrackSigmaTofK'),
    sigmaTofP = cms.InputTag('trackExtenderWithMTD', 'generalTrackSigmaTofP'),
    trackMVAQual = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    outermostHitPositionSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackOutermostHitPosition'),
    trackMinimumPt = cms.double(0.7),
    trackMaximumPt = cms.double(12),
    trackMaximumBtlEta = cms.double(1.5),
    trackMinimumEtlEta = cms.double(1.6),
    trackMaximumEtlEta = cms.double(3),
    optionalPlots = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod