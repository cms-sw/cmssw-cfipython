import FWCore.ParameterSet.Config as cms

def BTagSkimLeptonJet(*args, **kwargs):
  mod = cms.EDFilter('BTagSkimLeptonJet',
    CaloJet = cms.InputTag('iterativeCone5CaloJets'),
    MinimumCaloJetPt = cms.double(20),
    MinimumPtRel = cms.double(0),
    LeptonType = cms.string(''),
    Lepton = cms.InputTag(''),
    MinimumNLeptonJet = cms.int32(1),
    MaximumDeltaR = cms.double(0.4),
    MaximumLeptonEta = cms.double(2.5),
    MinimumLeptonPt = cms.double(6),
    MaximumCaloJetEta = cms.double(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
