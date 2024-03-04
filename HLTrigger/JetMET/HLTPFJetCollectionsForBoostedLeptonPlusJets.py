import FWCore.ParameterSet.Config as cms

def HLTPFJetCollectionsForBoostedLeptonPlusJets(**kwargs):
  mod = cms.EDProducer('HLTPFJetCollectionsForBoostedLeptonPlusJets',
    HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
    SourceJetTag = cms.InputTag('jetCollection'),
    minDeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
