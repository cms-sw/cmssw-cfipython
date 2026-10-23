import FWCore.ParameterSet.Config as cms

def HLTPFJetsCleanedFromLeadingLeptons(*args, **kwargs):
  mod = cms.EDProducer('HLTPFJetsCleanedFromLeadingLeptons',
    leptons = cms.InputTag('triggerFilterObjectWithRefs'),
    jets = cms.InputTag('jetCollection'),
    minDeltaR = cms.double(0.3),
    numLeptons = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
