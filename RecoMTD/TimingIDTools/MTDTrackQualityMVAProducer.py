import FWCore.ParameterSet.Config as cms

def MTDTrackQualityMVAProducer(**kwargs):
  mod = cms.EDProducer('MTDTrackQualityMVAProducer',
    tracksSrc = cms.InputTag('generalTracks'),
    btlMatchChi2Src = cms.InputTag('trackExtenderWithMTD', 'btlMatchChi2'),
    btlMatchTimeChi2Src = cms.InputTag('trackExtenderWithMTD', 'btlMatchTimeChi2'),
    etlMatchChi2Src = cms.InputTag('trackExtenderWithMTD', 'etlMatchChi2'),
    etlMatchTimeChi2Src = cms.InputTag('trackExtenderWithMTD', 'etlMatchTimeChi2'),
    mtdTimeSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
    pathLengthSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackPathLength'),
    npixBarrelSrc = cms.InputTag('trackExtenderWithMTD', 'npixBarrel'),
    npixEndcapSrc = cms.InputTag('trackExtenderWithMTD', 'npixEndcap'),
    qualityBDT_weights_file = cms.FileInPath('RecoMTD/TimingIDTools/data/clf4D_MTDquality_bo.xml'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
