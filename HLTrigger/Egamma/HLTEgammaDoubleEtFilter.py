import FWCore.ParameterSet.Config as cms

def HLTEgammaDoubleEtFilter(**kwargs):
  mod = cms.EDFilter('HLTEgammaDoubleEtFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltTrackIsolFilter'),
    l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
    etcut1 = cms.double(30),
    etcut2 = cms.double(20),
    npaircut = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
