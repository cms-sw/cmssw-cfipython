import FWCore.ParameterSet.Config as cms

mtdTrackQualityMVAProducer = cms.EDProducer('MTDTrackQualityMVAProducer',
  tracksSrc = cms.InputTag('generalTracks'),
  tracksMTDSrc = cms.InputTag('trackExtenderWithMTD'),
  btlMatchChi2Src = cms.InputTag('trackExtenderWithMTD', 'btlMatchChi2'),
  btlMatchTimeChi2Src = cms.InputTag('trackExtenderWithMTD', 'btlMatchTimeChi2'),
  etlMatchChi2Src = cms.InputTag('trackExtenderWithMTD', 'etlMatchChi2'),
  etlMatchTimeChi2Src = cms.InputTag('trackExtenderWithMTD', 'etlMatchTimeChi2'),
  mtdTimeSrc = cms.InputTag('trackExtenderWithMTD', 'tmtd'),
  pathLengthSrc = cms.InputTag('trackExtenderWithMTD', 'pathLength'),
  trackAssocSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackassoc'),
  qualityBDT_weights_file = cms.FileInPath('RecoMTD/TimingIDTools/data/clf4D_MTDquality_bo.xml'),
  mightGet = cms.optional.untracked.vstring
)
