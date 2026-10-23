import FWCore.ParameterSet.Config as cms

def HLTPFJetCollectionsForElePlusJets(*args, **kwargs):
  mod = cms.EDProducer('HLTPFJetCollectionsForElePlusJets',
    HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
    SourceJetTag = cms.InputTag('jetCollection'),
    minDeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
