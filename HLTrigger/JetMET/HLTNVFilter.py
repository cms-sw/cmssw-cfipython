import FWCore.ParameterSet.Config as cms

def HLTNVFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTNVFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('iterativeCone5CaloJets'),
    inputMETTag = cms.InputTag('hlt1MET60'),
    minEtJet2 = cms.double(20),
    minEtJet1 = cms.double(80),
    minNV = cms.double(0.1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
