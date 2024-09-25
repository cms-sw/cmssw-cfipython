import FWCore.ParameterSet.Config as cms

def HLTCaloJetsMatchedToFilteredPFJetsProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTCaloJetsMatchedToFilteredPFJetsProducer',
    src = cms.InputTag('hltJets'),
    triggerJetsFilter = cms.InputTag('hltCaloJetsFiltered'),
    triggerJetsType = cms.int32(85),
    maxDeltaR = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
