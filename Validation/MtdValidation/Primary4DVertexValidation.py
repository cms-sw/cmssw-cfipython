import FWCore.ParameterSet.Config as cms

def Primary4DVertexValidation(*args, **kwargs):
  mod = cms.EDProducer('Primary4DVertexValidation',
    folder = cms.string('MTD/Vertices'),
    TPtoRecoTrackAssoc = cms.InputTag('trackingParticleRecoTrackAsssociation'),
    mtdTracks = cms.InputTag('trackExtenderWithMTD'),
    SimTag = cms.InputTag('mix', 'MergedTrackTruth'),
    offlineBS = cms.InputTag('offlineBeamSpot'),
    offline4DPV = cms.InputTag('offlinePrimaryVertices4D'),
    trackAssocSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackassoc'),
    pathLengthSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackPathLength'),
    momentumSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackp'),
    tmtd = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
    timeSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
    sigmaSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmatmtd'),
    t0PID = cms.InputTag('tofPID', 't0'),
    sigmat0PID = cms.InputTag('tofPID', 'sigmat0'),
    t0SafePID = cms.InputTag('tofPID', 't0safe'),
    sigmat0SafePID = cms.InputTag('tofPID', 'sigmat0safe'),
    trackMVAQual = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    tofPi = cms.InputTag('trackExtenderWithMTD', 'generalTrackTofPi'),
    tofK = cms.InputTag('trackExtenderWithMTD', 'generalTrackTofK'),
    tofP = cms.InputTag('trackExtenderWithMTD', 'generalTrackTofP'),
    probPi = cms.InputTag('tofPID', 'probPi'),
    probK = cms.InputTag('tofPID', 'probK'),
    probP = cms.InputTag('tofPID', 'probP'),
    useOnlyChargedTracks = cms.bool(True),
    optionalPlots = cms.untracked.bool(False),
    use3dNoTime = cms.bool(False),
    trackweightTh = cms.double(0.5),
    mvaTh = cms.double(0.8),
    minProbHeavy = cms.double(0.75),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
