import FWCore.ParameterSet.Config as cms

def MTDTrackQualityMVAProducer(*args, **kwargs):
  mod = cms.EDProducer('MTDTrackQualityMVAProducer',
    tracksSrc = cms.InputTag('generalTracks'),
    btlMatchChi2Src = cms.InputTag('trackExtenderWithMTD', 'btlMatchChi2'),
    btlMatchTimeChi2Src = cms.InputTag('trackExtenderWithMTD', 'btlMatchTimeChi2'),
    etlMatchChi2Src = cms.InputTag('trackExtenderWithMTD', 'etlMatchChi2'),
    etlMatchTimeChi2Src = cms.InputTag('trackExtenderWithMTD', 'etlMatchTimeChi2'),
    mtdTimeSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
    sigmamtdTimeSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmatmtd'),
    pathLengthSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackPathLength'),
    npixBarrelSrc = cms.InputTag('trackExtenderWithMTD', 'npixBarrel'),
    npixEndcapSrc = cms.InputTag('trackExtenderWithMTD', 'npixEndcap'),
    outermostHitPositionSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackOutermostHitPosition'),
    offlineBS = cms.InputTag('offlineBeamSpot'),
    qualityBDT_weights_file = cms.FileInPath('RecoMTD/TimingIDTools/data/BDT_nvars_17_d7.xml'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
