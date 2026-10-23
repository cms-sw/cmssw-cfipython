import FWCore.ParameterSet.Config as cms

def TauValidator(*args, **kwargs):
  mod = cms.EDProducer('TauValidator',
    genTauCollection = cms.InputTag('tauGenJets'),
    recoTauCollection = cms.InputTag('hltHpsPFTauProducer'),
    recoTauIDCollections = cms.VInputTag(
      'hltHpsPFTauDeepTauProducer:VSjet',
      'hltHpsPFTauDeepTauProducer:VSe',
      'hltHpsPFTauDeepTauProducer:VSmu'
    ),
    cutIDs_raw = cms.vdouble(
      0,
      0,
      0
    ),
    cutIDs_wp = cms.vint32(
      -1,
      -1,
      -1
    ),
    minDeltaR = cms.double(0.3),
    outFolder = cms.string('HLT/Tau/TauValidation'),
    isPatTaus = cms.untracked.bool(False),
    TauPreSelection = cms.PSet(
      PtMinGenCut = cms.double(0),
      EtaMaxGenCut = cms.double(3),
      PtMinRecoCut = cms.double(20),
      EtaMaxRecoCut = cms.double(3)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
