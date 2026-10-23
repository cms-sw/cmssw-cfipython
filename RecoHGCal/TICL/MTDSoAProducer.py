import FWCore.ParameterSet.Config as cms

def MTDSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('MTDSoAProducer',
    tracksSrc = cms.InputTag('generalTracks'),
    trackAssocSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackassoc'),
    t0Src = cms.InputTag('tofPID', 't0'),
    sigmat0Src = cms.InputTag('tofPID', 'sigmat0'),
    tmtdSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
    sigmatmtdSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmatmtd'),
    betamtd = cms.InputTag('trackExtenderWithMTD', 'generalTrackBeta'),
    pathmtd = cms.InputTag('trackExtenderWithMTD', 'generalTrackPathLength'),
    mvaquality = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    posmtd = cms.InputTag('trackExtenderWithMTD', 'generalTrackmtdpos'),
    momentum = cms.InputTag('trackExtenderWithMTD', 'generalTrackp'),
    probPi = cms.InputTag('tofPID', 'probPi'),
    probK = cms.InputTag('tofPID', 'probK'),
    probP = cms.InputTag('tofPID', 'probP'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
