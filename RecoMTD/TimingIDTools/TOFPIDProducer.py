import FWCore.ParameterSet.Config as cms

def TOFPIDProducer(**kwargs):
  mod = cms.EDProducer('TOFPIDProducer',
    tracksSrc = cms.InputTag('generalTracks'),
    t0Src = cms.InputTag('trackExtenderWithMTD', 'generalTrackt0'),
    tmtdSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracktmtd'),
    sigmat0Src = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmat0'),
    sigmatmtdSrc = cms.InputTag('trackExtenderWithMTD', 'generalTracksigmatmtd'),
    tofkSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackTofK'),
    tofpSrc = cms.InputTag('trackExtenderWithMTD', 'generalTrackTofP'),
    vtxsSrc = cms.InputTag('unsortedOfflinePrimaryVertices4DwithPID'),
    trackMTDTimeQualityVMapTag = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    vtxMaxSigmaT = cms.double(0.025),
    maxDz = cms.double(0.1),
    maxDtSignificance = cms.double(5),
    minProbHeavy = cms.double(0.75),
    fixedT0Error = cms.double(0),
    probPion = cms.double(1),
    probKaon = cms.double(1),
    probProton = cms.double(1),
    minTrackTimeQuality = cms.double(0.8),
    MVASel = cms.bool(False),
    vertexReassignment = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod