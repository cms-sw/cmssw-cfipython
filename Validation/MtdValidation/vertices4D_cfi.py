import FWCore.ParameterSet.Config as cms

vertices4D = cms.EDProducer('Primary4DVertexValidation',
  folder = cms.string('MTD/Vertices'),
  TPtoRecoTrackAssoc = cms.InputTag('trackingParticleRecoTrackAsssociation'),
  mtdTracks = cms.InputTag('trackExtenderWithMTD'),
  SimTag = cms.InputTag('mix', 'MergedTrackTruth'),
  offlineBS = cms.InputTag('offlineBeamSpot'),
  offline4DPV = cms.InputTag('offlinePrimaryVertices4D'),
  trackAssocSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackassoc'),
  pathLengthSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackPathLength'),
  momentumSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackp'),
  timeSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
  sigmaSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmatmtd'),
  t0SafePID = cms.InputTag('tofPID', 't0safe'),
  sigmat0SafePID = cms.InputTag('tofPID', 'sigmat0safe'),
  trackMVAQual = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
  useOnlyChargedTracks = cms.bool(True),
  debug = cms.untracked.bool(False),
  optionalPlots = cms.untracked.bool(False),
  trackweightTh = cms.double(0.5),
  mvaTh = cms.double(0.01),
  lineDensityPar = cms.vdouble(
    1.87,
    0,
    42.5
  ),
  mightGet = cms.optional.untracked.vstring
)
