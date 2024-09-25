import FWCore.ParameterSet.Config as cms

def HLTAcoFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTAcoFilter',
    saveTags = cms.bool(True),
    inputJetTag = cms.InputTag('IterativeCone5CaloJets'),
    inputMETTag = cms.InputTag('MET'),
    minDeltaPhi = cms.double(0),
    maxDeltaPhi = cms.double(2),
    minEtJet1 = cms.double(20),
    minEtJet2 = cms.double(20),
    Acoplanar = cms.string('Jet1Jet2'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
