import FWCore.ParameterSet.Config as cms

def HLTCaloJetCollectionsForLeptonPlusJets(**kwargs):
  mod = cms.EDProducer('HLTCaloJetCollectionsForLeptonPlusJets',
    HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
    SourceJetTag = cms.InputTag('caloJetCollection'),
    minDeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
