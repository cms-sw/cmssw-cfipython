import FWCore.ParameterSet.Config as cms

def HLTCaloJetCollectionsForElePlusJets(**kwargs):
  mod = cms.EDProducer('HLTCaloJetCollectionsForElePlusJets',
    HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
    SourceJetTag = cms.InputTag('jetCollection'),
    minDeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
