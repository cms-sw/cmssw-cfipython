import FWCore.ParameterSet.Config as cms

mtdTracks = cms.EDProducer('MtdTracksValidation',
  folder = cms.string('MTD/Tracks'),
  inputTagG = cms.InputTag('generalTracks'),
  inputTagT = cms.InputTag('trackExtenderWithMTD'),
  inputTagV = cms.InputTag('offlinePrimaryVertices4D'),
  tmtd = cms.InputTag('trackExtenderWithMTD', 'tmtd'),
  sigmatmtd = cms.InputTag('trackExtenderWithMTD', 'sigmatmtd'),
  t0Src = cms.InputTag('trackExtenderWithMTD', 'generalTrackt0'),
  sigmat0Src = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmat0'),
  trackAssocSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackassoc'),
  pathLengthSrc = cms.InputTag('trackExtenderWithMTD', 'pathLength'),
  t0SafePID = cms.InputTag('tofPID', 't0safe'),
  sigmat0SafePID = cms.InputTag('tofPID', 'sigmat0safe'),
  sigmat0PID = cms.InputTag('tofPID', 'sigmat0'),
  t0PID = cms.InputTag('tofPID', 't0'),
  trackMVAQual = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
  trackMinimumPt = cms.double(1),
  trackMinimumEta = cms.double(1.5),
  trackMaximumEta = cms.double(3.2),
  mightGet = cms.optional.untracked.vstring
)