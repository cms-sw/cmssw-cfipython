import FWCore.ParameterSet.Config as cms

def HLTElectronMuonInvMassFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTElectronMuonInvMassFilter',
    saveTags = cms.bool(True),
    elePrevCandTag = cms.InputTag('hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandDphiFilter'),
    muonPrevCandTag = cms.InputTag('hltL1Mu0HTT50L3Filtered3'),
    lowerMassCut = cms.double(4),
    upperMassCut = cms.double(999999),
    ncandcut = cms.int32(1),
    electronRelaxed = cms.untracked.bool(True),
    ElectronL1IsoCand = cms.InputTag('hltPixelMatchElectronsActivity'),
    ElectronL1NonIsoCand = cms.InputTag('hltPixelMatchElectronsActivity'),
    MuonCand = cms.InputTag('hltL3MuonCandidates'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
