import FWCore.ParameterSet.Config as cms

def HLTCaloJetsCleanedFromLeadingLeptons(**kwargs):
  mod = cms.EDProducer('HLTCaloJetsCleanedFromLeadingLeptons',
    leptons = cms.InputTag('triggerFilterObjectWithRefs'),
    jets = cms.InputTag('jetCollection'),
    minDeltaR = cms.double(0.3),
    numLeptons = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
