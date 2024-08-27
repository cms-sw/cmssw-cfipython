import FWCore.ParameterSet.Config as cms

def HLTPFTauPairLeadTrackDzMatchFilter(**kwargs):
  mod = cms.EDFilter('HLTPFTauPairLeadTrackDzMatchFilter',
    saveTags = cms.bool(True),
    tauSrc = cms.InputTag('hltPFTaus'),
    tauMinPt = cms.double(5),
    tauMaxEta = cms.double(2.5),
    tauMinDR = cms.double(0.1),
    tauLeadTrackMaxDZ = cms.double(0.2),
    triggerType = cms.int32(84),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
