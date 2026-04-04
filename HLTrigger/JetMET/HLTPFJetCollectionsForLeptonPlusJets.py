import FWCore.ParameterSet.Config as cms

def HLTPFJetCollectionsForLeptonPlusJets(*args, **kwargs):
  mod = cms.EDProducer('HLTPFJetCollectionsForLeptonPlusJets',
    HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
    SourceJetTag = cms.InputTag('caloJetCollection'),
    minDeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
