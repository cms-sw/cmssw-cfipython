import FWCore.ParameterSet.Config as cms

tofPIDProducer = cms.EDProducer('TOFPIDProducer',
  tracksSrc = cms.InputTag('generalTracks'),
  t0Src = cms.InputTag('trackExtenderWithMTD', 'generalTrackt0'),
  tmtdSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
  sigmat0Src = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmat0'),
  sigmatmtdSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmatmtd'),
  tofkSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackTofK'),
  tofpSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackTofP'),
  vtxsSrc = cms.InputTag('unsortedOfflinePrimaryVertices4DwithPID'),
  vtxMaxSigmaT = cms.double(0.025),
  maxDz = cms.double(0.1),
  maxDtSignificance = cms.double(5),
  minProbHeavy = cms.double(0.75),
  fixedT0Error = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
