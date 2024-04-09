import FWCore.ParameterSet.Config as cms

def HLTEcalCandidatePFMTFilter(**kwargs):
  mod = cms.EDFilter('HLTEcalCandidatePFMTFilter',
    saveTags = cms.bool(True),
    inputMetTag = cms.InputTag('hltPFMHT'),
    inputEleTag = cms.InputTag('hltEle25CaloIdVTTrkIdTCaloIsoTTrkIsoTTrackIsolFilter'),
    l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
    minN = cms.int32(0),
    minMht = cms.double(0),
    lowerMTCut = cms.double(0),
    upperMTCut = cms.double(9999),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod