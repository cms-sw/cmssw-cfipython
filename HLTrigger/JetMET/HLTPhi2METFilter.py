import FWCore.ParameterSet.Config as cms

def HLTPhi2METFilter(**kwargs):
  mod = cms.EDFilter('HLTPhi2METFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('iterativeCone5CaloJets'),
    inputMETTag = cms.InputTag('hlt1MET60'),
    minDeltaPhi = cms.double(0.377),
    minEtJet2 = cms.double(60),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
